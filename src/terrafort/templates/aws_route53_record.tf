
resource "aws_route53_record" "{{ resource.Name | trim(".") | replace(".", "_") | replace("-", "_") | lower }}_{{ resource.Type }}" {
      zone_id = aws_route53_zone.{{ resource.ZoneName | trim(".") | replace(".", "_") }}.id
      name = "{{ resource.Name }}"
      type = "{{ resource.Type }}"
      {%- if resource.TTL %}
      ttl = "{{ resource.TTL }}"
      {% endif %}
      {%- if resource.ResourceRecords %}
      records = [
      {%- for record in resource.ResourceRecords %}
      {{ "\"%s\",\n" % (record.Value) }}
      {%- endfor -%}
      ]
      {% endif %}
      {%- if resource.AliasTarget %}
      alias {
      name = "{{ resource.AliasTarget.DNSName }}"
      zone_id = "{{ resource.AliasTarget.HostedZoneId }}"
      evaluate_target_health = "{{ resource.AliasTarget.EvaluateTargetHealth }}"
      }
      {%- endif %}
}

