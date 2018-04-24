#!/usr/bin/env python3

import stacks


class Stack_Factory:

    factories = {}

    @staticmethod
    def stack_extract():

        for _stack_subclass in stacks.ABCSTACK.__subclasses__():
            _stack_class = _stack_subclass.stack_class
            Stack_Factory.factories[_stack_class] = _stack_subclass.Factory()

    @staticmethod
    def stack_create(stack_class, application_name):

        _stack_class_lower = stack_class.lower()

        if not Stack_Factory.factories:
            Stack_Factory.stack_extract()

        if _stack_class_lower not in Stack_Factory.factories.keys():
            raise LookupError('Invalid Stack Id %s' % _stack_class_lower)

        return Stack_Factory.factories[_stack_class_lower].create(application_name).create_stack()

    @staticmethod
    def stack_update(stack_class, application_name):

        _stack_class_lower = stack_class.lower()

        if not Stack_Factory.factories:
            Stack_Factory.stack_extract()

        if _stack_class_lower not in Stack_Factory.factories.keys():
            raise LookupError('Invalid Stack Id %s' % _stack_class_lower)

        return Stack_Factory.factories[_stack_class_lower].create(application_name).update_stack()

    @staticmethod
    def stack_delete(stack_class, application_name):

        _stack_class_lower = stack_class.lower()

        if not Stack_Factory.factories:
            Stack_Factory.stack_extract()

        if _stack_class_lower not in Stack_Factory.factories.keys():
            raise LookupError('Invalid Stack Id %s' % _stack_class_lower)

        return Stack_Factory.factories[_stack_class_lower].create(application_name).delete_stack()

# if __name__ == '__main__':
#     fact = Stack_Factory()
#     fact.stack_extract()
