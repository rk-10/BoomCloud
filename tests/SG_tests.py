from stack_functions.securitygroup_functions import SecurityGroupFunctions
from troposphere.ec2 import SecurityGroupRule,SecurityGroup
import pytest


def test_ingress_rule():
    assert isinstance(SecurityGroupFunctions.create_sg_ingress_rule("https"), SecurityGroupRule)


def test_final_sg_rule():
    assert isinstance(SecurityGroupFunctions.create_sg("rohan"), SecurityGroup)


# if __name__ == '__main__':
#     unittest.main()
