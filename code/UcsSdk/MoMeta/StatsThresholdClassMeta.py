import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"StatsClassId":UcsPropertyMeta("StatsClassId", "statsClassId", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x40L, None, None, None, ["adaptorEthPortBySizeLargeStats", "adaptorEthPortBySizeSmallStats", "adaptorEthPortErrStats", "adaptorEthPortMcastStats", "adaptorEthPortOutsizedStats", "adaptorEthPortStats", "adaptorEtherIfStats", "adaptorFcIfEventStats", "adaptorFcIfFC4Stats", "adaptorFcIfFrameStats", "adaptorFcPortStats", "adaptorMenloBaseErrorStats", "adaptorMenloDcePortStats", "adaptorMenloEthErrorStats", "adaptorMenloEthStats", "adaptorMenloFcErrorStats", "adaptorMenloFcStats", "adaptorMenloHostPortStats", "adaptorMenloMcpuErrorStats", "adaptorMenloMcpuStats", "adaptorMenloNetEgStats", "adaptorMenloNetInStats", "adaptorMenloQErrorStats", "adaptorMenloQStats", "adaptorVnicStats", "computeIOHubEnvStats", "computeMbPowerStats", "computeMbTempStats", "computePCIeFatalCompletionStats", "computePCIeFatalProtocolStats", "computePCIeFatalReceiveStats", "computePCIeFatalStats", "computeRackUnitMbTempStats", "equipmentChassisStats", "equipmentFanModuleStats", "equipmentFanStats", "equipmentFexEnvStats", "equipmentFexPowerSummary", "equipmentFexPsuInputStats", "equipmentIOCardStats", "equipmentNetworkElementFanStats", "equipmentPsuInputStats", "equipmentPsuOutputStats", "equipmentPsuStats", "equipmentRackUnitFanStats", "equipmentRackUnitPsuStats", "etherErrStats", "etherFcoeInterfaceStats", "etherLossStats", "etherPauseStats", "etherRxStats", "etherTxStats", "fcErrStats", "fcStats", "memoryArrayEnvStats", "memoryBufferUnitEnvStats", "memoryErrorStats", "memoryRuntime", "memoryUnitEnvStats", "powerGroupStats", "processorEnvStats", "processorErrorStats", "processorRuntime", "swCardEnvStats", "swEnvStats", "swSystemStats", "unspecified"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("StatsThresholdClass", "statsThresholdClass", "[StatsClassId]", _VersionMeta.Version101e, "InputOutput", 0xffL, [], [u'statsThr32Definition', u'statsThr64Definition', u'statsThrFloatDefinition'], ["Add", "Get", "Remove", "Set"], ["admin", "operations"])
}

