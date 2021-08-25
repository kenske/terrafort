resource "aws_route53_zone" "{{ resource.Name | trim(".") | replace(".", "_") }}" {
  name    = "{{ resource.Name | trim(".") }}"
  comment = "{{ resource.Config.Comment }}"
}