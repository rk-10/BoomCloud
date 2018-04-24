from stack_functions.route53_functions import Route53_functions
from stacks.ABC_stack import ABCSTACK


class Stack_Route53(ABCSTACK):

    stack_class = 'route53'

    class Factory:
        @staticmethod
        def create(application_name): return Stack_Route53()

    def stack_name(self):

        name = 'r53stack'
        return name

    def build_child_template(self):

        hzvpc = Route53_functions.hosted_zone_vpc('vpcroute53', vpcid=self.vpcid_fetch(),
                                                       vpc_region=self._az_region[0])
        _hz = Route53_functions.hosted_zone('Hostedzone', domain_name='rohan.newzify.com', vpcs=[hzvpc])
        self.add_resource_to_template(_hz)

