from apiclient.exceptions import APIClientError
from terrafort.renderer import Renderer


class VercelProjectEnvironmentVariables:
    """
    Render a template for a project's environment variables
    """

    def __init__(self, client, project_id, team_id, use_map, git_branch, production):
        self.client = client
        self.project_id = project_id
        self.team_id = team_id
        self.git_branch = git_branch
        self.use_map = use_map
        self.production = production

    def render(self, commands=False):

        try:
            variables = self.client.get_environment_variables(self.project_id, self.team_id, self.git_branch)
            project = self.client.get_project(self.project_id, self.team_id)
        except APIClientError as error:
            print(error)
            return None

        template = 'vercel_project_environment_variable.tf' if not self.use_map \
            else 'vercel_project_environment_variable_map.tf'
        fmt_enabled = False

        if commands:
            template = 'vercel_project_environment_variable.import.j2' if not self.use_map \
                else 'vercel_project_environment_variable_map.import.j2'
            fmt_enabled = False

        if self.production:
            envs = []
            for env in variables['envs']:
                if 'production' in env['target']:
                    envs.append(env)
            variables['envs'] = envs

        renderer = Renderer(fmt_enabled=fmt_enabled)

        if self.use_map:
            variables['git_branch'] = self.git_branch

        variables['project_id'] = self.project_id
        variables['team_id'] = self.team_id
        variables['project_name'] = project['name']

        output = renderer.render(variables, "vercel/%s" % template)

        return output
