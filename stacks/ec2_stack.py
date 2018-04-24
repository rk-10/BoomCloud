from stack_functions.ec2_functions import EC2_functions
from stack_functions.securitygroup_functions import SecurityGroupFunctions
from stacks.ABC_stack import ABCSTACK
from troposphere import FindInMap
from troposphere import Ref
import troposphere.ec2 as ec2

class EC2(ABCSTACK):

    stack_class = 'ec2'

    class Factory:
        @staticmethod
        def create(application_name): return EC2()

    def stack_name(self):
        name ='EC2'
        return name

    @staticmethod
    def instance_name():
        name = 'TestingEC2'
        return name

    def build_child_template(self):

        template = ABCSTACK.get_template(self)

        security_group = SecurityGroupFunctions.create_sg("SGviaSDK")

        EC2_functions.add_mapping_to_template(template)

        instance = ec2.Instance(
            EC2.instance_name(),
            ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
            InstanceType="t2.micro",
            KeyName=Ref(EC2_functions.add_keyname_param_to_template(template)),
            SecurityGroups=[Ref(self.add_resource_to_template(security_group))],
        )

        self.add_resource_to_template(instance)
        EC2_functions.add_ec2_output(template, instance)

        # print(template.to_json())

#
# if __name__ == '__main__':
#     ec21 = EC2()
#     ec21.build_child_template()




