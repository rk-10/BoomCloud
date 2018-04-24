#!/usr/bin/env python3

import getopt
import sys

from stack_factory.factory import Stack_Factory

class BoomCloud:

    def __init__(self):

        self.stack_class = None
        self.operation = None
        self.application_name = None

        self.get_opt()

    def get_opt(self):

        try:
            opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "stack=", "operation=" ,"application-name="])
        except getopt.GetoptError as err:
            print(err)
            usage()
            sys.exit(2)
        verbose = False
        for o, a in opts:
            if o == "-v":
                verbose = True
            elif o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o == "--stack":
                self.stack_class = a
            elif o == "--operation":
                self.operation = a
            elif o =="--application-name":
                self.application_name = a
            else:
                assert False, "unhandled option"

    def boom_Stack(self):

        if self.operation == 'create':
            Stack_Factory.stack_create(self.stack_class, self.application_name)
        elif self.operation == 'update':
            Stack_Factory.stack_update(self.stack_class, self.application_name)
        elif self.operation == 'delete':
            Stack_Factory.stack_delete(self.stack_class, self.application_name)
        else:
            raise LookupError('Invalid operation')

# Entry point for the application
if __name__ == '__main__':
    boom = BoomCloud()
    boom.boom_Stack()

def usage():
    print('Option not recognized')
