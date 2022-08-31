{% for variable in resource.envs %}

# ID: {{ variable.id }}
resource "vercel_project_environment_variable" "{{ resource.project_name | lower | replace("-", "_") }}_{{ variable.target[0] }}_{{ variable.key | lower | trim(".") | replace("-", "_") }}" {
  key        = "{{ variable.key }}"
  project_id = "{{ resource.project_id }}"
  team_id    = "{{ resource.team_id }}"
  value      = "secret"
  target     = {{ variable.target | replace ("'", "\"") }}
  {%- if variable.gitBranch %}
  git_branch = "{{ variable.gitBranch }}"
  {%- endif %}
}

{%- endfor %}