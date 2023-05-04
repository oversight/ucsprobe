import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Bitmask":UcsPropertyMeta("Bitmask", "bitmask", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"CollInterval":UcsPropertyMeta("CollInterval", "collInterval", "ushort", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ContClassId":UcsPropertyMeta("ContClassId", "contClassId", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["compute:Board", "memory:Unit", "processor:Unit", "unspecified"], ["0-4294967295"]),
	"ContInstId":UcsPropertyMeta("ContInstId", "contInstId", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unspecified"], ["0-4294967295"]),
	"ContInstIdPropId":UcsPropertyMeta("ContInstIdPropId", "contInstIdPropId", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["memory:Unit:id", "processor:Unit:id", "unspecified"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"EqptClassId":UcsPropertyMeta("EqptClassId", "eqptClassId", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["compute:Board", "memory:Unit", "processor:Unit", "unspecified"], ["0-4294967295"]),
	"EqptInstId":UcsPropertyMeta("EqptInstId", "eqptInstId", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unspecified"], ["0-4294967295"]),
	"EqptInstIdPropId":UcsPropertyMeta("EqptInstIdPropId", "eqptInstIdPropId", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["memory:Unit:id", "processor:Unit:id", "unspecified"], ["0-4294967295"]),
	"GlobalId":UcsPropertyMeta("GlobalId", "globalId", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LocalId":UcsPropertyMeta("LocalId", "localId", "uint", _VersionMeta.Version111j, UcsPropertyMeta.Naming, 0x4L, None, None, None, [], ["0-4294967295"]),
	"PcGlobalId":UcsPropertyMeta("PcGlobalId", "pcGlobalId", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["No Errors"], ["0-4294967295"]),
	"PcLocalId":UcsPropertyMeta("PcLocalId", "pcLocalId", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["No Errors"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"StatsClassId":UcsPropertyMeta("StatsClassId", "statsClassId", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["compute:PCIeFatalCompletionStats", "compute:PCIeFatalProtocolStats", "compute:PCIeFatalReceiveStats", "compute:PCIeFatalStats", "memory:ErrorStats", "processor:ErrorStats", "unspecified"], ["0-4294967295"]),
	"StatsPropId":UcsPropertyMeta("StatsPropId", "statsPropId", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["compute:PCIeFatalCompletionStats:AbortErrors", "compute:PCIeFatalCompletionStats:TimeoutErrors", "compute:PCIeFatalCompletionStats:unexpectedErrors", "compute:PCIeFatalProtocolStats:dllpErrors", "compute:PCIeFatalProtocolStats:flowControlErrors", "compute:PCIeFatalReceiveStats:bufferOverflowErrors", "compute:PCIeFatalReceiveStats:errFatalErrors", "compute:PCIeFatalReceiveStats:errNonFatalErrors", "compute:PCIeFatalReceiveStats:unsupportedRequestErrors", "compute:PCIeFatalStats:acsViolationErrors", "compute:PCIeFatalStats:malformedTLPErrors", "compute:PCIeFatalStats:poisonedTLPErrors", "compute:PCIeFatalStats:surpriseLinkDownErrors", "memory:ErrorStats:addressParityErrors", "memory:ErrorStats:eccMultibitErrors", "memory:ErrorStats:eccSinglebitErrors", "memory:ErrorStats:mismatchErrors", "processor:ErrorStats:mirroringInterSockErrors", "processor:ErrorStats:mirroringIntraSockErrors", "processor:ErrorStats:smiLinkCorrErrors", "processor:ErrorStats:smiLinkUncorrErrors", "processor:ErrorStats:sparingErrors", "unspecified"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Threshold":UcsPropertyMeta("Threshold", "threshold", "ushort", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Value":UcsPropertyMeta("Value", "value", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("BmcSELCounter", "bmcSELCounter", "Counter-[LocalId]", _VersionMeta.Version111j, "InputOutput", 0x1fL, [], [], ["Get"], ["read-only"])
}

