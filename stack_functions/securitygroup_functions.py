from troposphere.ec2 import SecurityGroup,SecurityGroupRule
from troposphere import Template


class SecurityGroupFunctions:

    _sg_ingress = {
        "ssh": "22",
        "http": "80",
        "https": "443"
    }

    _cidr_ip = "0.0.0.0/0"


    @staticmethod
    def create_sg_ingress_rule(_type):

        if _type.lower() not in ["ssh","http","https"]:
            raise ValueError("Wrong key value given")

        _sg_ingress_rule = SecurityGroupRule(
            IpProtocol="tcp",
            FromPort=SecurityGroupFunctions._sg_ingress[_type.lower()],
            ToPort=SecurityGroupFunctions._sg_ingress[_type.lower()],
            CidrIp=SecurityGroupFunctions._cidr_ip
        )

        # print(_sg_ingress_rule)
        return _sg_ingress_rule


    @staticmethod
    def create_sg(sg_title):

        _sg_ingress = []

        for i in ["ssh", "http", "https"]:
            _sg_ingress.append(SecurityGroupFunctions.create_sg_ingress_rule(i))

        _sg = SecurityGroup(
            sg_title,
            GroupDescription="Enable ssh, http and https access",
            SecurityGroupIngress=_sg_ingress
        )
        # t = Template()
        # t.add_resource(_sg)
        # print(t.to_json())
        return _sg


if __name__ == '__main__':
    sg = SecurityGroupFunctions()
    # sg.create_sg_ingress_rule("http")
    # sg.create_sg("yo")
