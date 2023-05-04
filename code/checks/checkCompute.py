'''
Created on Apr 14, 2016

@author: sjuul
'''
from generic.checks.checkResponse import CheckResponse
from core.ucsCheckBase import UcsCheckBase
from core.testCheck import testCheck
from UcsSdk.MoMeta.ComputeBlade import ComputeBlade
from UcsSdk.MoMeta.ComputeMbPowerStats import ComputeMbPowerStats
from UcsSdk.MoMeta.ComputeMbTempStats import ComputeMbTempStats
from UcsSdk.MoMeta.EquipmentHealthLed import EquipmentHealthLed
from checks import tryFloat
from checks import parseTimeIfAny
from checks import yesBl
from checks import equipedBl
from checks import operableBl
from checks import availBl
from checks import inServiceBl
from checks import onBl
from checks import okBl


#  ComputeHealthLedSensorAlarm  !!!


class CheckCompute(UcsCheckBase):
    
    CLASS_FORMATTERS = {
        ComputeMbTempStats: {
            'FmTempSenRear': tryFloat,
            'Suspect': ('isSuspect', yesBl),
            'FmTempSenRearLAvg': tryFloat,
            'TimeCollected': parseTimeIfAny,
            'FmTempSenRearMax': tryFloat,
            'Update': int,
            'FmTempSenIo': tryFloat,
            'FmTempSenIoMin': tryFloat,
            'FmTempSenRearAvg': tryFloat,
            'FmTempSenIoAvg': tryFloat,
            'FmTempSenRearL': tryFloat,
            'FmTempSenRearRAvg': tryFloat,
            'FmTempSenIoMax': tryFloat,
            'FmTempSenRearRMin': tryFloat,
            'FmTempSenRearRMax': tryFloat,
            'Intervals': int,
            'FmTempSenRearMin': tryFloat,
            'FmTempSenRearLMax': tryFloat
        },
        ComputeMbPowerStats: {
            'ConsumedPowerAvg': tryFloat,
            'InputCurrentMax': tryFloat,
            'InputVoltage': tryFloat,
            'InputVoltageMax': tryFloat,
            'Update': int,
            'Intervals': int,
            'Suspect': ('isSuspect', yesBl),
            'ConsumedPowerMax': tryFloat,
            'InputCurrentMin': tryFloat,
            'InputCurrent': tryFloat,
            'ConsumedPower': tryFloat,
            'TimeCollected': parseTimeIfAny,
            'ConsumedPowerMin': tryFloat,
            'InputCurrentAvg': tryFloat,
            'InputVoltageMin': tryFloat,
            'InputVoltageAvg': tryFloat
        }, ComputeBlade: {
            'AvailableMemory': int,
            'OperPower': ('isPoweredOn', onBl),
            'TotalMemory': int,
            'NumOfEthHostIfs': int,
            'OperState': ('operStateIsOk', okBl),
            'NumOfCpus': int,
            'NumOfCores': int,
            'LcTs': parseTimeIfAny,
            'NumOfFcHostIfs': int,
            'NumOfCoresEnabled': int,
            'AdminState': ('AdminStateIsInService', inServiceBl),
            'NumOfThreads': int,
            'MemorySpeed': int,
            'Presence': ('isEquipped', equipedBl),
            'MfgTime': parseTimeIfAny,
            'Operability': ('operabilityIsOperable', operableBl),
            'Availability': ('isAvailable', availBl)
        }, EquipmentHealthLed: {
            'OperState': ('OperStateIsOn', onBl),
            'Color': ('isGreen', lambda vl: vl == 'green'),
            'HealthLedState': ('HealthLedStateIsNormal', lambda vl: vl == 'normal')             
        }
    }
    
    def getData(self, config, callback, errback):
        cr = CheckResponse()
        for cls in (ComputeBlade, ComputeMbPowerStats, ComputeMbTempStats, EquipmentHealthLed):  
            data = self.connection.GetManagedObject(classId=cls.ClassId())
            fmtrs = self.CLASS_FORMATTERS.get(cls)
            cr.setTypeData(cls.__name__, {mo.Dn: self.moToDct(mo, fmtrs) for mo in data})
          
        return cr

if __name__ == '__main__':
    testCheck(CheckCompute, '172.22.0.151')