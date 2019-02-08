{% for range in resource.IpRanges %}
resource "aws_security_group_rule" "{{ resource.name }}-{{ count() }}" {
  security_group_id = "{{ resource.id }}"
  type              = "{{ resource.type }}"
  from_port         = {{ resource.FromPort | default('0')}}
  to_port           = {{ resource.ToPort | default('0')}}
  protocol          = "{{ resource.IpProtocol}}"
  cidr_blocks       = ["{{ range.CidrIp }}"]
  description       = "{{ range.Description }}"
}

{% endfor %}

{% for source in resource.UserIdGroupPairs %}
resource "aws_security_group_rule" "{{ resource.name }}-{{ count() }}" {
  security_group_id        = "{{ resource.id }}"
  type                     = "{{ resource.type }}"
  from_port                = {{resource.FromPort | default('0')}}
  to_port                  = {{resource.ToPort| default('0')}}
  protocol                 = "{{ resource.IpProtocol}}"
  source_security_group_id = "{{ source.GroupId }}"
  description              = "{{ source.Description }}"
}

{% endfor %}