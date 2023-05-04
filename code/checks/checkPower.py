'''
Created on Apr 16, 2016

@author: sjuul
'''
from UcsSdk.MoMeta.PowerBudget import PowerBudget
from UcsSdk.MoMeta.PowerChassisMember import PowerChassisMember
from UcsSdk.MoMeta.EquipmentChassisStats import EquipmentChassisStats
from UcsSdk.MoMeta.EquipmentPsu import EquipmentPsu
from UcsSdk.MoMeta.EquipmentPsuStats import EquipmentPsuStats
from UcsSdk.MoMeta.LsPower import LsPower
from UcsSdk.MoMeta.ComputePsuControl import ComputePsuControl
from generic.checks.checkResponse import CheckResponse
from core.ucsCheckBase import UcsCheckBase
from core.testCheck import testCheck
from checks import parseTimeIfAny
from checks import okBl
from checks import tryFloat
from checks import yesBl
from checks import operableBl
from checks import equipedBl
from checks import isUpBl


class CheckPower(UcsCheckBase):
    
    CLASS_FORMATTERS = {
        PowerChassisMember: {
            'OperState': ('OperStateIsCapOk', lambda vl: vl == 'cap-ok')
        }, PowerBudget: {
            'AdminPeak': int,
            'IdlePower': int,
            'CatalogPower': int,
            'MinPower': int,
            'OperState': ('OperStateIsDeployed', lambda vl: vl == 'deployed'),
            'ScaledWt': int,
            'MaxPower': int,
            'UpdateTime': parseTimeIfAny,
            'OperPeak': int,
            'PsuState': ('PusStateIsOk', okBl),
            'PsuCapacity': int,
            'Weight': int,
            'CurrentPower': int,
            'OperCommitted': int,
            'OperMin': int,
            'AdminCommitted': int
        }, EquipmentChassisStats: {
            'OutputPower': tryFloat,
            'InputPower': tryFloat,
            'OutputPowerAvg': tryFloat,
            'Update': int,
            'OutputPowerMin': tryFloat,
            'Intervals': int,
            'Suspect': ('isSuspect', yesBl),
            'InputPowerMax': tryFloat,
            'InputPowerMin': tryFloat,
            'TimeCollected': parseTimeIfAny,
            'InputPowerAvg': tryFloat,
            'OutputPowerMax': tryFloat
        }, EquipmentPsu: {
            'OperState': ('operStateIsOperable', operableBl),
            'Presence': ('isEquipped', equipedBl),
            'Thermal': ('thermalIsOk', okBl),
            'Operability': ('operabilityIsOperable', operableBl)
        }, EquipmentPsuStats: {
            'OutputPower': tryFloat,
            'OutputCurrentAvg': tryFloat,
            'Output12vMin': tryFloat,
            'Output3v3': tryFloat,
            'Suspect': ('isSuspect', yesBl),
            'TimeCollected': parseTimeIfAny,
            'OutputCurrent': tryFloat,
            'Output12v': tryFloat,
            'Output12vMax': tryFloat,
            'Update': int,
            'AmbientTempAvg': tryFloat,
            'Output3v3Avg': tryFloat,
            'PsuTemp2': tryFloat,
            'Input210vMax': tryFloat,
            'PsuTemp1': tryFloat,
            'OutputPowerMax': tryFloat,
            'Output3v3Min': tryFloat,
            'AmbientTempMin': tryFloat,
            'OutputCurrentMax': tryFloat,
            'Output3v3Max': tryFloat,
            'OutputPowerMin': tryFloat,
            'AmbientTemp': tryFloat,
            'Input210v': tryFloat,
            'Input210vMin': tryFloat,
            'AmbientTempMax': tryFloat,
            'Output12vAvg': tryFloat,
            'OutputPowerAvg': tryFloat,
            'OutputCurrentMin': tryFloat,
            'Intervals': int,
            'Input210vAvg': tryFloat
        }, ComputePsuControl: {
            'OutputPowerState': ('OutputPowerStateIsOk', okBl),
            'OperState': ('operStateIsOk', okBl),
            'InputPowerState': ('InputPowerStateIsOk', okBl)
        }, LsPower: {
            "State": ('StateIsUp', isUpBl),
        }         
    }
    
    def getData(self, config, callback, errback):
        cr = CheckResponse()
        for cls in (PowerBudget, PowerChassisMember, EquipmentChassisStats, EquipmentPsu, EquipmentPsuStats, LsPower, ComputePsuControl):  
            data = self.connection.GetManagedObject(classId=cls.ClassId())
            fmtrs = self.CLASS_FORMATTERS.get(cls)
            cr.setTypeData(cls.__name__, {mo.Dn: self.moToDct(mo, fmtrs) for mo in data})
          
        return cr

if __name__ == '__main__':
    testCheck(CheckPower, '172.22.0.151')