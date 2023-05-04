"""
file is generated with probeCreator
"""
from six import with_metaclass
from generic.root.probeRoot import GenericProbeRootMixin
from generic.singleton import Singleton
from core.version import Version


class Root(with_metaclass(Singleton, GenericProbeRootMixin)):
    """ Program information. """

    version = Version

    def __init__(self):
        super(Root, self).__init__(
            myName="ucsProbe",
            probeProperties=[]
        )
