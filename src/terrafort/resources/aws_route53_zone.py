import boto3
import pprint
import json
from botocore.exceptions import ClientError
from terrafort.renderer import Renderer


class AwsRoute53Zone:
    """
    Render a template for a Route53 zone and all its records.
    """

    def __init__(self, zone_id):
        self.client = boto3.client('route53')
        self.zone_id = zone_id

    def render(self, commands=False):
        """
        Using one template for the security group, and another for rules.
        :return:
        """
        try:
            zone_response = self.client.get_hosted_zone(Id=self.zone_id)
            records_response = self.client.list_resource_record_sets(HostedZoneId=self.zone_id)
        except ClientError as error:
            print(error)
            return None

        renderer = Renderer()
        zone = zone_response['HostedZone']
        zone_template = 'aws_route53_zone.tf'
        record_template = 'aws_route53_record.tf'
        if commands:
            zone_template = 'aws_route53_zone.import.j2'
            record_template = 'aws_route53_record.import.j2'
            renderer = Renderer(fmt_enabled=False)

        output = renderer.render(zone, zone_template)

        # print(json.dumps(zone_response, indent=2))
        # exit(0)


        renderer.reset_count()  # Need this to add a numeric suffix to each rule name
        for record in records_response['ResourceRecordSets']:
            if record["Type"] in ["NS", "SOA"]:
                continue
            record["ZoneName"] = zone["Name"]
            record["ZoneId"] = self.zone_id
            output += renderer.render(record, record_template)

        return output
