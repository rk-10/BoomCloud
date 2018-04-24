from troposphere import Base64, FindInMap, GetAtt
from troposphere import Parameter, Output, Ref, Template
import troposphere.ec2 as ec2

class EC2_functions:

    ami_mapping = {
        "us-east-1": {"AMI": "ami-7f418316"},
        "us-west-1": {"AMI": "ami-951945d0"},
        "us-east-2": {"AMI": "ami-2581aa40"},
        # "eu-west-1": {"AMI": "ami-24506250"},
        # "sa-east-1": {"AMI": "ami-3e3be423"},
        # "ap-southeast-1": {"AMI": "ami-74dda626"},
        # "ap-northeast-1": {"AMI": "ami-dcfa4edd"}
    }


    @staticmethod
    def add_mapping_to_template(template: Template):

        template.add_mapping('RegionMap', EC2_functions.ami_mapping)

    @staticmethod
    def add_ec2_output(template, ec2_instance):
        template.add_output([
            Output(
                "InstanceId",
                Description="InstanceId of the newly created EC2 instance",
                Value=Ref(ec2_instance),
            ),
            Output(
                "AZ",
                Description="Availability Zone of the newly created EC2 instance",
                Value=GetAtt(ec2_instance, "AvailabilityZone"),
            ),
            Output(
                "PublicIP",
                Description="Public IP address of the newly created EC2 instance",
                Value=GetAtt(ec2_instance, "PublicIp"),
            ),
            Output(
                "PrivateIP",
                Description="Private IP address of the newly created EC2 instance",
                Value=GetAtt(ec2_instance, "PrivateIp"),
            ),
            Output(
                "PublicDNS",
                Description="Public DNSName of the newly created EC2 instance",
                Value=GetAtt(ec2_instance, "PublicDnsName"),
            ),
            Output(
                "PrivateDNS",
                Description="Private DNSName of the newly created EC2 instance",
                Value=GetAtt(ec2_instance, "PrivateDnsName"),
            ),
        ])


    @staticmethod
    def add_keyname_param_to_template(template: Template):

        keyname_param = Parameter(
            "KeyName",
            Type="String",
            Default="Myec2keypair",
            Description="Name of an existing EC2 KeyPair to enable SSH "
                        "access to the instance",

        )

        _keyname_param = template.add_parameter(keyname_param)

        return _keyname_param

    