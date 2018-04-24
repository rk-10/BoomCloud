from troposphere.ec2 import VPC, InternetGateway, Subnet, VPCGatewayAttachment, Route, RouteTable, \
    SubnetRouteTableAssociation, VPCEndpoint


class Vpcfunctions:

    @staticmethod
    def create_vpc(vpc_title, vpc_cidr=None):

        if vpc_cidr is None:
            vpc_cidr = '10.0.1.0/24'

        _vpc = VPC(title=vpc_title, CidrBlock=vpc_cidr, EnableDnsSupport=True, EnableDnsHostnames=True)

        return _vpc

    @staticmethod
    def create_subnet(_subnet_title, _vpcid=None, _availability_zone=None, _map_public_ip_on_launch=False,
                      _subnet_cidr=None):

        _sbnet = Subnet(title=_subnet_title, CidrBlock=_subnet_cidr, VpcId=_vpcid,
                        AvailabilityZone=_availability_zone, MapPublicIpOnLaunch=_map_public_ip_on_launch)

        return _sbnet

    @staticmethod
    def create_igw(_igw_title):

        _igw = InternetGateway(title=_igw_title)

        return _igw

    @staticmethod
    def vpc_igw_attachment(vpcigw_title, vpc_id=None, igwid=None):

        vpc_igw_attachment = VPCGatewayAttachment(title=vpcigw_title, InternetGatewayId=igwid, VpcId=vpc_id)

        return vpc_igw_attachment

    @staticmethod
    def create_route_table(rt_title, vpcid=None):

        _route_table = RouteTable(title=rt_title, VpcId=vpcid)

        return _route_table

    @staticmethod
    def create_route(_title, igw=None, dest_cidr=None, route_table_id=None):

        _route = Route(title=_title, DestinationCidrBlock=dest_cidr, GatewayId=igw, RouteTableId=route_table_id)

        return _route

    @staticmethod
    def create_subnet_route_table_association(sn_rt_title, routetableid=None, subnetid=None):

        _subnet_routetable_association = SubnetRouteTableAssociation(title=sn_rt_title, RouteTableId=routetableid,
                                                                     SubnetId=subnetid)

        return _subnet_routetable_association

    @staticmethod
    def create_vpc_endpoint(vpc_endpt_title, route_tableid, _vpcid, _service_name):

        _vpc_endpt = VPCEndpoint(title=vpc_endpt_title, RouteTableIds=route_tableid, VpcId=_vpcid,
                                 ServiceName=_service_name)

        return _vpc_endpt
