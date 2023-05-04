'''
file is generated with probeCreator
'''

from generic.checks.checkFactory import GenericCheckFactory
from generic.singleton import Singleton
from checks.checkCompute import CheckCompute
from checks.checkFabric import CheckFabric
from checks.checkFans import CheckFans
from checks.checkIoCard import CheckIoCard
from checks.checkNetwork import CheckNetwork
from checks.checkPower import CheckPower
from checks.checkStorage import CheckStorage
from checks.checkSystem import CheckSystem


class UcsCheckFactory(GenericCheckFactory):
    ''' Builds checks, dynamic class generation.'''
    __metaclass__ = Singleton

    def __init__(self, basePath):
        constructors = {
            'CheckCompute': CheckCompute,
            'CheckFabric': CheckFabric,
            'CheckFans': CheckFans,
            'CheckIoCard': CheckIoCard,
            'CheckNetwork': CheckNetwork,
            'CheckPower': CheckPower,
            'CheckStorage': CheckStorage, 
            'CheckSystem': CheckSystem 
        }
        super(UcsCheckFactory, self).__init__(checkKwargs={'basePath': basePath}, constructors=constructors)
