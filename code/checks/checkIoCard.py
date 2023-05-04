'''
Created on Apr 21, 2016

@author: sjuul
'''
from UcsSdk.MoMeta.EquipmentIOCard import EquipmentIOCard
from UcsSdk.MoMeta.EquipmentIOCardStats import EquipmentIOCardStats
from generic.checks.checkResponse import CheckResponse
from core.ucsCheckBase import UcsCheckBase
from core.testCheck import testCheck
from checks import okBl
from checks import parseTimeIfAny
from checks import onlineBl
from checks import operableBl
from checks import equipedBl
from checks import connectedBl
from checks import tryFloat
from checks import yesBl



class CheckIoCard(UcsCheckBase):
    
    CLASS_FORMATTERS = {
        EquipmentIOCard: {
            'Discovery': ('DiscoveryIsOnline', onlineBl),
            'OperState': ('OperStateIsOperable', operableBl),
            'ConfigState': ('ConfigStateIsOk', okBl),
            'LcTs': parseTimeIfAny,
            'Operability': ('OperabilityIsOperable', operableBl),
            'Presence': ('PresenceIsEquipped', equipedBl),
            'MfgTime': parseTimeIfAny,
            'Thermal': ('ThermalIsOk', okBl),
            'PeerCommStatus': ('PeerCommStatusIsConnected', connectedBl)
        }, EquipmentIOCardStats: {
            'Temp': tryFloat,
            'AmbientTempMax': tryFloat,
            'AmbientTempMin': tryFloat,
            'TempAvg': tryFloat,
            'Update': int,
            'AmbientTempAvg': tryFloat,
            'TempMin': tryFloat,
            'Intervals': int,
            'Suspect': ('isSuspect', yesBl),
            'AmbientTemp': tryFloat,
            'TimeCollected': parseTimeIfAny,
            'TempMax': tryFloat
        }
    }
    
    def getData(self, config, callback, errback):
        cr = CheckResponse()
        for cls in (EquipmentIOCard, EquipmentIOCardStats):  
            data = self.connection.GetManagedObject(classId=cls.ClassId())
            fmtrs = self.CLASS_FORMATTERS.get(cls)
            cr.setTypeData(cls.__name__, {mo.Dn: self.moToDct(mo, fmtrs) for mo in data})
          
        return cr

if __name__ == '__main__':
    testCheck(CheckIoCard, '172.22.0.151')