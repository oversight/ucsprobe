'''
Created on Apr 14, 2016

@author: sjuul
'''
from UcsSdk.MoMeta.SwEthLanEp import SwEthLanEp
from UcsSdk.MoMeta.EquipmentSwitchCard import EquipmentSwitchCard
from UcsSdk.MoMeta.AdaptorExtEthIf import AdaptorExtEthIf
from UcsSdk.MoMeta.EtherRxStats import EtherRxStats
from UcsSdk.MoMeta.EtherSwitchIntFIo import EtherSwitchIntFIo
from UcsSdk.MoMeta.EtherTxStats import EtherTxStats
from UcsSdk.MoMeta.NetworkElement import NetworkElement
from generic.checks.checkResponse import CheckResponse
from core.ucsCheckBase import UcsCheckBase
from core.testCheck import testCheck
from checks import parseTimeIfAny
from checks import yesBl
from checks import enabledBl
from checks import operableBl
from checks import onlineBl
from checks import isUpBl
from checks import presentBl
from UcsSdk.MoMeta.IppoolBlock import IppoolBlock
from UcsSdk.MoMeta.SwAccessEp import SwAccessEp
from UcsSdk.MoMeta.SwEnvStats import SwEnvStats
from checks import tryFloat
from UcsSdk.MoMeta.ExtmgmtIf import ExtmgmtIf


xStats = {
    'UnicastPacketsDelta': int,
    'BroadcastPackets': int,
    'JumboPacketsDeltaMin': int,
    'MulticastPackets': int,
    'Intervals': int,
    'BroadcastPacketsDeltaAvg': int,
    'BroadcastPacketsDelta': int,
    'JumboPacketsDeltaMax': int,
    'TotalBytesDelta': int,
    'MulticastPacketsDeltaAvg': int,
    'Suspect': ('isSuspect', yesBl),
    'TotalBytesDeltaMax': int,
    'TimeCollected': parseTimeIfAny,
    'MulticastPacketsDeltaMax': int,
    'UnicastPacketsDeltaAvg': int,
    'TotalBytes': int,
    'Update': int,
    'TotalPacketsDeltaMax': int,
    'BroadcastPacketsDeltaMin': int,
    'JumboPacketsDelta': int,
    'TotalPacketsDeltaMin': int,
    'JumboPackets': int,
    'TotalPacketsDelta': int,
    'UnicastPackets': int,
    'BroadcastPacketsDeltaMax': int,
    'TotalBytesDeltaAvg': int,
    'TotalPackets': int,
    'UnicastPacketsDeltaMin': int,
    'UnicastPacketsDeltaMax': int,
    'MulticastPacketsDeltaMin': int,
    'TotalBytesDeltaMin': int,
    'MulticastPacketsDelta': int,
    'TotalPacketsDeltaAvg': int,
    'JumboPacketsDeltaAvg': int
}


def operStateChanged(dct):
    dct['operStateChanged'] = dct.get('OperState') != dct.get('LastOperStateReport')


class CheckNetwork(UcsCheckBase):
    
    CLASS_FORMATTERS = {
        SwEthLanEp: {
            'UdldAdminState': ('UdldAdminStateEnabled', enabledBl),
            'AdminState': ('AdminStateEnabled', enabledBl) 
        },
        EquipmentSwitchCard: {
            'State': ('stateIsOnline', onlineBl),
            'Operability': ('isOperable', operableBl),
            'Power': ('isPoweredOn', onlineBl),
            'Ts': parseTimeIfAny,
            'NumPorts': int                
        },
        EtherTxStats: xStats,
        EtherRxStats: xStats,
        EtherSwitchIntFIo: {
            'Ts': parseTimeIfAny,
            'Discovery': ('isPresent', presentBl),
            'OperState': ('operStateIsUp', isUpBl),
            'AdminState': ('AdminStateEnabled', enabledBl)
        },
        AdaptorExtEthIf: {
            'LinkState': ('isUp', isUpBl),
            'Discovery': ('isPresent', presentBl),
            'AdminState': ('AdminStateEnabled', enabledBl)
        }, SwAccessEp: {
            'AdminState': ('AdminStateEnabled', enabledBl)
        }, SwEnvStats: {
            'FanCtrlrInlet3Avg': tryFloat,
            'FanCtrlrInlet1': tryFloat,
            'PsuCtrlrInlet1Avg': tryFloat,
            'Suspect': ('isSuspect', yesBl),
            'PsuCtrlrInlet1Max': tryFloat,
            'TimeCollected': parseTimeIfAny,
            'FanCtrlrInlet2Max': tryFloat,
            'FanCtrlrInlet1Avg': tryFloat,
            'FanCtrlrInlet3Max': tryFloat,
            'Update': int,
            'FanCtrlrInlet2': tryFloat,
            'FanCtrlrInlet3': tryFloat,
            'MainBoardOutlet2Max': tryFloat,
            'PsuCtrlrInlet2Max': tryFloat,
            'PsuCtrlrInlet2Avg': tryFloat,
            'FanCtrlrInlet4Avg': tryFloat,
            'FanCtrlrInlet4Max': tryFloat,
            'MainBoardOutlet2Min': tryFloat,
            'PsuCtrlrInlet1': tryFloat,
            'FanCtrlrInlet4Min': tryFloat,
            'MainBoardOutlet1Max': tryFloat,
            'MainBoardOutlet1Avg': tryFloat,
            'FanCtrlrInlet2Avg': tryFloat,
            'MainBoardOutlet1Min': tryFloat,
            'FanCtrlrInlet1Max': tryFloat,
            'FanCtrlrInlet3Min': tryFloat,
            'MainBoardOutlet2': tryFloat,
            'MainBoardOutlet1': tryFloat,
            'PsuCtrlrInlet2Min': tryFloat,
            'PsuCtrlrInlet2': tryFloat,
            'PsuCtrlrInlet1Min': tryFloat,
            'FanCtrlrInlet1Min': tryFloat,
            'FanCtrlrInlet4': tryFloat,
            'Intervals': int,
            'FanCtrlrInlet2Min': tryFloat,
            'MainBoardOutlet2Avg': tryFloat
        }, ExtmgmtIf: {
            'OperState': ('operStateIsUp', isUpBl),
            'FailReportCount': int,
        } 
    }
    
    def getData(self, config, callback, errback):
        cr = CheckResponse()
        for cls in (SwAccessEp, SwEnvStats, SwEthLanEp, NetworkElement, AdaptorExtEthIf, EtherSwitchIntFIo, EquipmentSwitchCard, IppoolBlock, ExtmgmtIf):   
            data = self.connection.GetManagedObject(classId=cls.ClassId())
            fmtrs = self.CLASS_FORMATTERS.get(cls)
            cr.setTypeData(cls.__name__, {mo.Dn: self.moToDct(mo, fmtrs) for mo in data})
            #if data:
            #    print data[0]
        
        for cls in (EtherRxStats, EtherTxStats):
            data = self.connection.GetManagedObject(classId=cls.ClassId())
            fmtrs = self.CLASS_FORMATTERS.get(cls)
            cr.setTypeData(cls.__name__, {mo.Dn: self.moToDct(mo, fmtrs) for mo in data if not mo.Dn.startswith('sys/chassis-')})
        
        cr.mapFunToType('ExtmgmtIf', operStateChanged)
        
        return cr

if __name__ == '__main__':
    testCheck(CheckNetwork, '172.22.0.151')