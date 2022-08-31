from apiclient import (
    APIClient,
    endpoint,
)


@endpoint(base_url="https://api.vercel.com")
class Endpoint:
    project = "/v9/projects/{project_id}?teamId={team_id}"
    project_env = "/v9/projects/{project_id}/env?teamId={team_id}"


class Vercel(APIClient):
    def get_project(self, project_id, team_id):
        url = Endpoint.project.format(project_id=project_id, team_id=team_id)
        return self.get(url)

    def get_environment_variables(self, project_id, team_id, git_branch):
        url = Endpoint.project_env.format(project_id=project_id, team_id=team_id)
        params = {}
        if git_branch:
            params = {"gitBranch": git_branch}

        return self.get(url, params)

