'''
Created on Apr 21, 2016

@author: sjuul
'''
from generic.checks.checkResponse import CheckResponse
from core.ucsCheckBase import UcsCheckBase
from core.testCheck import testCheck
from UcsSdk.MoMeta.FabricChassisEp import FabricChassisEp
from UcsSdk.MoMeta.FabricEthLanPc import FabricEthLanPc
from UcsSdk.MoMeta.FabricEthLanPcEp import FabricEthLanPcEp
from UcsSdk.MoMeta.FabricFcSan import FabricFcSan
from checks import isUpBl
from checks import enabledBl
from checks import okBl



class CheckFabric(UcsCheckBase):
    
    CLASS_FORMATTERS = {
        FabricEthLanPcEp: {
            'LicState': ('licenseOk', lambda vl: vl == 'license-ok'),
            'OperState': ('OperstateIsUp', isUpBl),
            'Membership': ('MembershipIsUp', isUpBl),
            'AdminState': ('AdminStateIsEnabled', enabledBl)
        }, FabricFcSan: {
            'UplinkTrunking': ('UplinkTrunkingEnabled', enabledBl)
        }, FabricEthLanPc: {
            'OperState': ('OperstateIsUp', isUpBl),
            'VlanStatus': ('VlanStatusIsOk', okBl),
            'AdminState': ('AdminStateIsEnabled', enabledBl),
            'Bandwidth': int,
        }, FabricChassisEp: {
            'OperState': ('OperstateIsUp', isUpBl),
            'AdminState': ('AdminStateIsEnabled', enabledBl),
        }
    }
    
    def getData(self, config, callback, errback):
        cr = CheckResponse()
        for cls in (FabricChassisEp, FabricEthLanPc, FabricEthLanPcEp, FabricFcSan):  
            data = self.connection.GetManagedObject(classId=cls.ClassId())
            fmtrs = self.CLASS_FORMATTERS.get(cls)
            cr.setTypeData(cls.__name__, {mo.Dn: self.moToDct(mo, fmtrs) for mo in data})
          
        return cr

if __name__ == '__main__':
    testCheck(CheckFabric, '172.22.0.151')