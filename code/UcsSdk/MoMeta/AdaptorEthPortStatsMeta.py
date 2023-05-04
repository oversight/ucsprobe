import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"GoodPackets":UcsPropertyMeta("GoodPackets", "goodPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"GoodPacketsDelta":UcsPropertyMeta("GoodPacketsDelta", "goodPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"GoodPacketsDeltaAvg":UcsPropertyMeta("GoodPacketsDeltaAvg", "goodPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"GoodPacketsDeltaMax":UcsPropertyMeta("GoodPacketsDeltaMax", "goodPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"GoodPacketsDeltaMin":UcsPropertyMeta("GoodPacketsDeltaMin", "goodPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PausePackets":UcsPropertyMeta("PausePackets", "pausePackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PausePacketsDelta":UcsPropertyMeta("PausePacketsDelta", "pausePacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PausePacketsDeltaAvg":UcsPropertyMeta("PausePacketsDeltaAvg", "pausePacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PausePacketsDeltaMax":UcsPropertyMeta("PausePacketsDeltaMax", "pausePacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PausePacketsDeltaMin":UcsPropertyMeta("PausePacketsDeltaMin", "pausePacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PerPriorityPausePackets":UcsPropertyMeta("PerPriorityPausePackets", "perPriorityPausePackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PerPriorityPausePacketsDelta":UcsPropertyMeta("PerPriorityPausePacketsDelta", "perPriorityPausePacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PerPriorityPausePacketsDeltaAvg":UcsPropertyMeta("PerPriorityPausePacketsDeltaAvg", "perPriorityPausePacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PerPriorityPausePacketsDeltaMax":UcsPropertyMeta("PerPriorityPausePacketsDeltaMax", "perPriorityPausePacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PerPriorityPausePacketsDeltaMin":UcsPropertyMeta("PerPriorityPausePacketsDeltaMin", "perPriorityPausePacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PppPackets":UcsPropertyMeta("PppPackets", "pppPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PppPacketsDelta":UcsPropertyMeta("PppPacketsDelta", "pppPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PppPacketsDeltaAvg":UcsPropertyMeta("PppPacketsDeltaAvg", "pppPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PppPacketsDeltaMax":UcsPropertyMeta("PppPacketsDeltaMax", "pppPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PppPacketsDeltaMin":UcsPropertyMeta("PppPacketsDeltaMin", "pppPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"TotalPackets":UcsPropertyMeta("TotalPackets", "totalPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TotalPacketsDelta":UcsPropertyMeta("TotalPacketsDelta", "totalPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TotalPacketsDeltaAvg":UcsPropertyMeta("TotalPacketsDeltaAvg", "totalPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TotalPacketsDeltaMax":UcsPropertyMeta("TotalPacketsDeltaMax", "totalPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TotalPacketsDeltaMin":UcsPropertyMeta("TotalPacketsDeltaMin", "totalPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TrafficDirection":UcsPropertyMeta("TrafficDirection", "trafficDirection", "string", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, ["rx", "tx", "unknown"], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"VlanPackets":UcsPropertyMeta("VlanPackets", "vlanPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"VlanPacketsDelta":UcsPropertyMeta("VlanPacketsDelta", "vlanPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"VlanPacketsDeltaAvg":UcsPropertyMeta("VlanPacketsDeltaAvg", "vlanPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"VlanPacketsDeltaMax":UcsPropertyMeta("VlanPacketsDeltaMax", "vlanPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"VlanPacketsDeltaMin":UcsPropertyMeta("VlanPacketsDeltaMin", "vlanPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorEthPortStats", "adaptorEthPortStats", "eth-port-stats-[TrafficDirection]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [u'adaptorEthPortStatsHist'], ["Get"], ["admin", "operations", "read-only"])
}

