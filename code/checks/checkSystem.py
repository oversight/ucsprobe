'''
Created on Apr 14, 2016

@author: sjuul
'''
from UcsSdk.MoMeta.MgmtEntity import MgmtEntity
from UcsSdk.MoMeta.EquipmentChassis import EquipmentChassis
from UcsSdk.MoMeta.EquipmentHealthLed import EquipmentHealthLed
from core.ucsCheckBase import UcsCheckBase
from core.testCheck import testCheck
from generic.checks.checkResponse import CheckResponse
from checks import parseTimeIfAny
from checks import operableBl
from checks import isUpBl
from checks import okBl
from UcsSdk.MoMeta.SyntheticFile import SyntheticFile
from UcsSdk.MoMeta.SyntheticDirectory import SyntheticDirectory
from UcsSdk.MoMeta.SyntheticTime import SyntheticTime
from UcsSdk.MoMeta.SyntheticFileSystem import SyntheticFileSystem
from UcsSdk.MoMeta.SysdebugEp import SysdebugEp
from UcsSdk.MoMeta.SysdebugCore import SysdebugCore
from UcsSdk.MoMeta.SysfileDigest import SysfileDigest
from UcsSdk.MoMeta.TopRoot import TopRoot
from UcsSdk.MoMeta.TopSystem import TopSystem
from UcsSdk.MoMeta.VersionEp import VersionEp


def getShassisNr(inp):
    return inp.split('/')[-1]


class CheckSystem(UcsCheckBase):
    
    CLASS_FORMATTERS = {
        EquipmentChassis: {
            'LcTs': parseTimeIfAny,
            'MfgTime': parseTimeIfAny, 
            'LicState': ('LicenseOk', lambda vl: vl == 'license-ok'),
            'OperState': ('operStateIsUp', isUpBl),
            'Power': ('PowerOk', okBl),
            'ConfigState': ('ConfigStateIsOk', okBl),
            'SeepromOperState': ('SeepromOperStateIsOperable', operableBl),
            'Thermal': ('thermalOk', okBl),
            'Operability': ('OperabilityIsOperable', operableBl)
        },MgmtEntity: {
            'SshAuthKeysSize': int,
            'State': ('StateIsUp', isUpBl),
            'Leadership': ('isPrimary', lambda vl: vl == 'primary'),
            'SshRootPubKeySize': int,
            'MgmtServicesState': ('MgmtServicesStateIsUp', isUpBl),
            'ChassisDeviceIoState2': ('ChassisDeviceIoState2IsOk', okBl),
            'ChassisDeviceIoState3': ('ChassisDeviceIoState3IsOk', okBl),
            'ChassisDeviceIoState1': ('ChassisDeviceIoState1IsOk', okBl),
            'SshKeyStatus': ('SshKeyMatched', lambda vl: vl == 'matched'),
            'HaReady': lambda vl: vl =='yes',
        }
    }
    
    def getData(self, config, callback, errback):
        cr = CheckResponse()
        # EquipmentChassis, MgmtEntity
        for cls in (EquipmentChassis, MgmtEntity, TopSystem, ):
            data = self.connection.GetManagedObject(classId=cls.ClassId())
            cr.setTypeData(cls.__name__, {mo.Dn: self.moToDct(mo, self.CLASS_FORMATTERS.get(cls)) for mo in data})

        st = cr.stateData
        chassisLookup = {getShassisNr(item['name']): item['UsrLbl'] for item in st.get('EquipmentChassis', {}).values()}

        for item in st.get('MgmtEntity', {}).values():
            for ky in chassisLookup:
                item[ky + 'UserLabel'] = chassisLookup[ky]

        return cr

if __name__ == '__main__':
    testCheck(CheckSystem, '172.22.0.151')