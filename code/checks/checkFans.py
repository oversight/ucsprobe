'''
Created on Apr 14, 2016

@author: sjuul
'''
from UcsSdk.MoMeta.EquipmentFan import EquipmentFan
from UcsSdk.MoMeta.EquipmentFanModule import EquipmentFanModule
from UcsSdk.MoMeta.EquipmentFanModuleStats import EquipmentFanModuleStats
from UcsSdk.MoMeta.EquipmentNetworkElementFanStats import EquipmentNetworkElementFanStats
from generic.checks.checkResponse import CheckResponse
from core.ucsCheckBase import UcsCheckBase
from core.testCheck import testCheck
from checks import parseTimeIfAny
from checks import yesBl
from checks import operableBl
from checks import equipedBl
from checks import onBl
from checks import okBl


class CheckFans(UcsCheckBase):
    
    CLASS_FORMATTERS = {
        EquipmentNetworkElementFanStats: {
            'DrivePercentageAvg': int,
            'DrivePercentage': int,
            'SpeedMax': int,
            'SpeedAvg': int,
            'Update': int,
            'DrivePercentageMax': int,
            'Intervals': int,
            'Suspect': ('isSuspect', yesBl),
            'SpeedMin': int,
            'TimeCollected': parseTimeIfAny,
            'Speed': int,
            'DrivePercentageMin': int
        }, EquipmentFan: {
            'OperState': ('operStateIsOperable', operableBl),
            'Power': ('isPoweredOn', onBl),
            'Presence': ('isEquipped', equipedBl),
            'Thermal': ('thermalOk', okBl),
            'Operability': ('operabilityIsOperable', operableBl),
        }, EquipmentFanModuleStats: {
            'AmbientTempMax': float,
            'AmbientTempMin': float,
            'Update': int,
            'AmbientTempAvg': float,
            'Intervals': int,
            'Suspect': ('isSuspect', yesBl),
            'AmbientTemp': float,
            'TimeCollected': parseTimeIfAny,
        }, EquipmentFanModule: {
            'OperState': ('operStateIsOperable', operableBl),
            'Voltage': ('voltageOk', okBl),
            'Power': ('isPoweredOn', onBl),
            'Presence': ('isEquipped', equipedBl),
            'MfgTime': parseTimeIfAny,
            'Thermal': ('thermalOk', okBl),
            'Operability': ('operabilityIsOperable', operableBl),
        }
    }
    
    def getData(self, config, callback, errback):
        cr = CheckResponse()
        for cls in (EquipmentFan, EquipmentFanModule, EquipmentFanModuleStats, EquipmentNetworkElementFanStats):  
            data = self.connection.GetManagedObject(classId=cls.ClassId())
            fmtrs = self.CLASS_FORMATTERS.get(cls)
            cr.setTypeData(cls.__name__, {mo.Dn: self.moToDct(mo, fmtrs) for mo in data})
          
        return cr

if __name__ == '__main__':
    testCheck(CheckFans, '172.22.0.151')