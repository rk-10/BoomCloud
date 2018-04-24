from stack_functions.vpc_functions import Vpcfunctions
from troposphere.ec2 import VPC, InternetGateway, Subnet, VPCGatewayAttachment, Route, RouteTable, \
    SubnetRouteTableAssociation, VPCEndpoint
import pytest


_az_list = ['us-east-1a', 'us-east-1c', 'us-east-1d']
_VPC_CIDR = '10.0.0.0/24'


def test_cidr(_cidr):
    ip, cidr_size = _cidr.split("/")
    ip_parts = ip.split(".")
    return len(ip_parts) == 4 and int(ip[0]) == 10 and test_cidr_size('/' + cidr_size) and all(0 <= int(parts) <= 255\
                                                                                               for parts in ip_parts)


def test_cidr_size(_cidr):
    _cidr_size = _cidr.split("/")
    return 16 <= int(_cidr_size[1]) <= 24


def test_vpc_class():
    _vpc = Vpcfunctions.create_vpc("MyVpc", _VPC_CIDR)
    assert isinstance(_vpc, VPC)


def test_subnet_class():
    return


# if __name__ == '__main__':
#     test_cidr("10.0.0.0/24")
