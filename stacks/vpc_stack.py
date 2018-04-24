from stack_functions.vpc_functions import Vpcfunctions
from stacks.ABC_stack import ABCSTACK
from troposphere import Ref


class Vpc_stack(ABCSTACK):

    stack_class = 'vpc'

    class Factory:
        @staticmethod
        def create(application_name): return Vpc_stack()

    def stack_name(self):

        self.name = 'vpcstack'
        return self.name


    def build_child_template(self):
        # VPC
        _vpc = Vpcfunctions.create_vpc('myvpc')
        self.add_resource_to_template(_vpc)

        # Subnets
        dmz_subnet = Vpcfunctions.create_subnet('dmz', _vpcid=Ref(_vpc),
                                                     _subnet_cidr='10.0.1.0/28',
                                                     _availability_zone=self._az_list[0],
                                                     _map_public_ip_on_launch=True)

        private_subnet = Vpcfunctions.create_subnet('private',
                                                         _vpcid=Ref(_vpc),
                                                         _subnet_cidr='10.0.1.16/28',
                                                         _availability_zone=self._az_list[1],
                                                         _map_public_ip_on_launch=False)

        pvt_internal_subnet = Vpcfunctions.create_subnet('privateinernal', _vpcid=Ref(_vpc),
                                                              _subnet_cidr='10.0.1.32/28',
                                                              _availability_zone=self._az_list[2],
                                                              _map_public_ip_on_launch=False)
        self.add_resource_to_template(dmz_subnet)
        self.add_resource_to_template(private_subnet)
        self.add_resource_to_template(pvt_internal_subnet)

        # InternetGateway
        internet_gw = Vpcfunctions.create_igw('IGW1')
        self.add_resource_to_template(internet_gw)

        # VPC-IGW attachment
        internet_gw_attachment = Vpcfunctions.vpc_igw_attachment('IGW1vpc', vpc_id=Ref(_vpc),
                                                                igwid=Ref(internet_gw))
        self.add_resource_to_template(internet_gw_attachment)

        # RouteTables
        routetable1 = Vpcfunctions.create_route_table('Routetable1', vpcid=Ref(_vpc))
        routetable2 = Vpcfunctions.create_route_table('Routetable2', vpcid=Ref(_vpc))

        self.add_resource_to_template(routetable1)
        self.add_resource_to_template(routetable2)

        # Routetable-Subnet attachment
        rt_sn_attach1 = Vpcfunctions.create_subnet_route_table_association('dmzrt1',
                                                                           routetableid=Ref(routetable1),
                                                                           subnetid=Ref(dmz_subnet))
        rt_sn_attach2 = Vpcfunctions.create_subnet_route_table_association('privatert2',
                                                                           routetableid=Ref(routetable2),
                                                                           subnetid=Ref(private_subnet))
        self.add_resource_to_template(rt_sn_attach1)
        self.add_resource_to_template(rt_sn_attach2)

        # Routes
        route1 = Vpcfunctions.create_route('dmzrt1route', igw=Ref(internet_gw),
                                           route_table_id=Ref(routetable1), dest_cidr='0.0.0.0/0')
        self.add_resource_to_template(route1)

        # s3-Endpoint
        s3vpcendpoint = Vpcfunctions.create_vpc_endpoint('s3endpoint', _vpcid=Ref(_vpc),
                                                         route_tableid=[Ref(routetable1), Ref(routetable2)],
                                                         _service_name=self.s3service[0])
        self.add_resource_to_template(s3vpcendpoint)




