'''
Created on Apr 21, 2016

@author: sjuul
'''
from UcsSdk.MoMeta.NfsMountInst import NfsMountInst
from UcsSdk.MoMeta.StorageController import StorageController
from UcsSdk.MoMeta.StorageLocalDisk import StorageLocalDisk
from generic.checks.checkResponse import CheckResponse
from core.ucsCheckBase import UcsCheckBase
from core.testCheck import testCheck
from checks import operableBl
from checks import onlineBl
from checks import equipedBl



class CheckStorage(UcsCheckBase):
    
    CLASS_FORMATTERS = {
        NfsMountInst: {
            'OperState': ('OperStateIsMounted', lambda vl: vl == 'mounted'),
            'ClientConfigState': ('ClientConfigStateIsRegistered', lambda vl: vl == 'registered'),
        }, StorageLocalDisk: {
            'DiskState': ('diskOnline', onlineBl),
            'PowerState': ('powerStateIsActive', lambda vl: vl == 'active'),
            'Presence': ('presenceIsEquipped', equipedBl),
            'BlockSize': int,
            'NumberOfBlocks': int,
            'Size': int,
            'Operability': ('operabilityIsOperable', operableBl)
        }, StorageController: {
            'RebuildRate': int,
            'Operability': ('operabilityIsOperable', operableBl),
            'ControllerStatus': ('ControllerStatusIsOptimal', lambda vl: vl =='optimal'),
            'OobInterfaceSupported': lambda vl: vl == 'yes',
            'Presence': ('presenceIsEquipped', equipedBl),
        }
    }
    
    def getData(self, config, callback, errback):
        cr = CheckResponse()
        for cls in (StorageLocalDisk, StorageController, NfsMountInst):  
            data = self.connection.GetManagedObject(classId=cls.ClassId())
            fmtrs = self.CLASS_FORMATTERS.get(cls)
            cr.setTypeData(cls.__name__, {mo.Dn: self.moToDct(mo, fmtrs) for mo in data})            
        
        return cr

if __name__ == '__main__':
    testCheck(CheckStorage, '172.22.0.151')