from abc import abstractmethod

from boto3 import client, resource
from troposphere import Template

class ABCSTACK:

    def __init__(self):
        self.ec2_client = client('ec2')
        self.cfn_resource = resource('cloudformation')
        self.cfn_client = client('cloudformation')
        self._az_list = []
        self._az_region = []
        for zone in self.ec2_client.describe_availability_zones()['AvailabilityZones']:
            if zone['State'] == 'available':
                self._az_list.append(zone['ZoneName'])
                self._az_region.append(zone['RegionName'])

        self.s3service = self.ec2_client.describe_vpc_endpoint_services()['ServiceNames']
        self._template = Template()
        self.operation_create = 'create'
        self.operation_update = 'update'
        self.operation_delete = 'delete'


    def add_resource_to_template(self, _resource):

        template = self._template.add_resource(_resource)
        return template

    def get_template(self):
        return self._template

    def build_template(self):
        self.build_child_template()

    @abstractmethod
    def build_child_template(self):
        raise NotImplementedError

    @abstractmethod
    def stack_name(self):
        raise NotImplementedError

    def vpcid_fetch(self):

        idvpc = self.cfn_resource.StackResource('vpcstack','myvpc').physical_resource_id
        return idvpc

    # def fetch_vpc_id(self):
    #     while True:
    #         stack = self.cfn_client.describe_stacks(StackName=self.stack_name())
    #         if len(stack.get('Stacks', None) > 0):
    #             stackcreation = True
    #             break
    #         else:
    #             time.sleep(5)
    #
    #     if stackcreation == True:
    #
    #         self._vpcid = self.cfn_resource.StackResource('vpcstack', 'myvpc').physical_resource_id
    #         return self._vpcid


    def create_stack(self):

        self.build_template()
        self.cfn_client.create_stack(StackName=self.stack_name(), TemplateBody=self._template.to_json(),
                                     DisableRollback=True)

    def update_stack(self):

        # TODO Add a check whether stack exists or not
        self.build_template()
        self.cfn_client.update_stack(StackName=self.stack_name(), TemplateBody=self._template.to_json(),
                                     DisableRollback=True)

    def delete_stack(self):

        self.cfn_client.delete_stack(StackName=self.stack_name())




