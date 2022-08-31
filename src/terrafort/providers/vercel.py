import click

from terrafort.resources.vercel_project_environment_variables import VercelProjectEnvironmentVariables
from ..clients.Vercel import Vercel as VercelClient
from apiclient import (
    HeaderAuthentication,
    JsonResponseHandler,
    JsonRequestFormatter
)
import os


class Vercel:

    def __init__(self):
        pass

    @staticmethod
    @click.command('vercel_project_environment_variables')
    @click.argument('project_id')
    @click.argument('team_id')
    @click.option('--use-map', is_flag=True, help="Use a single resource block with a for_each loop")
    @click.option('--git-branch', default="")
    @click.option('--production', is_flag=True, help="Fetch production variables")
    @click.pass_obj
    def vercel_project_environment_variables(ctx, project_id, team_id, use_map, git_branch, production):
        """
        Create vercel_project_environment_variable entries for all variables in a project
        :return:
        """
        if use_map and git_branch == "" and not production:
            print("Git branch is required when --use-map is enabled")
            exit(1)

        variables = VercelProjectEnvironmentVariables(
            Vercel.get_client(),
            project_id,
            team_id,
            use_map,
            git_branch,
            production
        )
        print(variables.render(ctx['commands']))

    @staticmethod
    def get_client():
        token = os.getenv('VERCEL_API_TOKEN')
        client = VercelClient(
            authentication_method=HeaderAuthentication(token=token),
            response_handler=JsonResponseHandler,
            request_formatter=JsonRequestFormatter
        )

        return client
