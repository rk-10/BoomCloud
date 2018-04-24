from troposphere.route53 import HostedZone, HostedZoneVPCs

class Route53_functions:

    @staticmethod
    def hosted_zone_vpc(hz_vpc_title, vpcid, vpc_region):

        hostedzonevpc = HostedZoneVPCs(VPCId=vpcid, VPCRegion=vpc_region)

        return hostedzonevpc

    @staticmethod
    def hosted_zone(_hostedzone_title, domain_name, vpcs):

        hostedzone = HostedZone(title = _hostedzone_title, Name=domain_name, VPCs=vpcs)

        return hostedzone