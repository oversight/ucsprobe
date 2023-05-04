"""
This module is used to create the windows service. See ServiceHandler class for more info.
"""
from generic.setup.serviceHandler import ServiceHandler
from ucsProbe import main

class Handler(ServiceHandler):
    def __init__(self):
        super(Handler, self).__init__()
        self.main = main

