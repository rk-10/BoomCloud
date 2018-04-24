from troposphere import iam
#TODO: Use awacs library

class IAM_functions:

    @staticmethod
    def get_policy_document(_resource):

        # TODO: These are hard coded policies. We should be able to create random policies.
        switcher = {
            "ec2" : {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Action": "ec2:*",
                            "Effect": "Allow",
                            "Resource": "*"
                        },
                        {
                            "Effect": "Allow",
                            "Action": "elasticloadbalancing:*",
                            "Resource": "*"
                        },
                        {
                            "Effect": "Allow",
                            "Action": "cloudwatch:*",
                            "Resource": "*"
                        },
                        {
                            "Effect": "Allow",
                            "Action": "autoscaling:*",
                            "Resource": "*"
                        },
                        {
                            "Effect": "Allow",
                            "Action": "iam:CreateServiceLinkedRole",
                            "Resource": "arn:aws:iam::*:role/aws-service-role/spot.amazonaws.com/AWSServiceRoleForEC2Spot*",
                            "Condition": {
                                "StringLike": {
                                    "iam:AWSServiceName": "spot.amazonaws.com"
                                }
                            }
                        },
                        {
                            "Effect": "Allow",
                            "Action": "iam:CreateServiceLinkedRole",
                            "Resource": "arn:aws:iam::*:role/aws-service-role/spotfleet.amazonaws.com/AWSServiceRoleForEC2Spot*",
                            "Condition": {
                                "StringLike": {
                                    "iam:AWSServiceName": "spotfleet.amazonaws.com"
                                }
                            }
                        },
                        {
                            "Effect": "Allow",
                            "Action": "iam:CreateServiceLinkedRole",
                            "Resource": "arn:aws:iam::*:role/aws-service-role/ec2scheduled.amazonaws.com/AWSServiceRoleForEC2Scheduled*",
                            "Condition": {
                                "StringLike": {
                                    "iam:AWSServiceName": "ec2scheduled.amazonaws.com"
                                }
                            }
                        },
                        {
                            "Effect": "Allow",
                            "Action": "iam:CreateServiceLinkedRole",
                            "Resource": "arn:aws:iam::*:role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing",
                            "Condition": {
                                "StringLike": {
                                    "iam:AWSServiceName": "elasticloadbalancing.amazonaws.com"
                                }
                            }
                        }
                    ]
            },
            "s3" : {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": "s3:*",
                            "Resource": "*"
                        }
                    ]
            }
        }

        return switcher.get(_resource)


    @staticmethod
    def create_policy(policy_name, policy_document):

        _policy = iam.Policy(
                PolicyName=policy_name,
                PolicyDocument=policy_document
            )

        return _policy


    @staticmethod
    def _Role(role_name, policies, service):

        role = iam.Role(
            role_name,
            AssumeRolePolicyDocument={"Statement": [{
                        "Effect": "Allow",
                        "Principal": {
                            "Service": [ service + ".amazonaws.com" ]
                        },
                        "Action": service + ":*"  #[ "sts:AssumeRole" ]
                    }]},
            Policies=policies
        )

        return role