
resource "vercel_project_environment_variable" "{{ resource.project_name | lower | replace("-", "_") }}" {
  for_each  = toset(local.vercel.{{ resource.project_name | lower | replace("-", "_") }})
  key        = each.key
  project_id = "{{ resource.project_id }}"
  team_id    = "{{ resource.team_id }}"
  value      = each.value
  target     = {{ resource.envs[0].target | replace ("'", "\"") }}
  {%- if resource.git_branch %}
  git_branch = "{{ resource.git_branch }}"
  {%- endif %}
}


locals {
  vercel = {
    env = {
{%- for variable in resource.envs | sort(attribute='key') %}
      {{ variable.key }} = "secret", # Id: {{ variable.id}} | Target: {{ variable.target | replace ("'", "\"") }}
{%- endfor %}
    }
  }
}