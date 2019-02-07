resource "aws_security_group" "rac-dev-sup" {
  name                   = "{{ resource.GroupName }}"
  description            = "{{ resource.Description }}"
  vpc_id                 = "{{ resource.VpcId }}"
  revoke_rules_on_delete = true

  tags {
    {% for tag in resource.Tags %} {{ tag.Key }} = "{{tag.Value}}"
    {% endfor %}
  }
}