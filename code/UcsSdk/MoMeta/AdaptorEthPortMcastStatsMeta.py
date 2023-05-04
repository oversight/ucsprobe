import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"BroadcastPackets":UcsPropertyMeta("BroadcastPackets", "broadcastPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BroadcastPacketsDelta":UcsPropertyMeta("BroadcastPacketsDelta", "broadcastPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BroadcastPacketsDeltaAvg":UcsPropertyMeta("BroadcastPacketsDeltaAvg", "broadcastPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BroadcastPacketsDeltaMax":UcsPropertyMeta("BroadcastPacketsDeltaMax", "broadcastPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BroadcastPacketsDeltaMin":UcsPropertyMeta("BroadcastPacketsDeltaMin", "broadcastPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MulticastPackets":UcsPropertyMeta("MulticastPackets", "multicastPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MulticastPacketsDelta":UcsPropertyMeta("MulticastPacketsDelta", "multicastPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MulticastPacketsDeltaAvg":UcsPropertyMeta("MulticastPacketsDeltaAvg", "multicastPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MulticastPacketsDeltaMax":UcsPropertyMeta("MulticastPacketsDeltaMax", "multicastPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MulticastPacketsDeltaMin":UcsPropertyMeta("MulticastPacketsDeltaMin", "multicastPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"TrafficDirection":UcsPropertyMeta("TrafficDirection", "trafficDirection", "string", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, ["rx", "tx", "unknown"], ["0-4294967295"]),
	"UnicastPackets":UcsPropertyMeta("UnicastPackets", "unicastPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnicastPacketsDelta":UcsPropertyMeta("UnicastPacketsDelta", "unicastPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnicastPacketsDeltaAvg":UcsPropertyMeta("UnicastPacketsDeltaAvg", "unicastPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnicastPacketsDeltaMax":UcsPropertyMeta("UnicastPacketsDeltaMax", "unicastPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UnicastPacketsDeltaMin":UcsPropertyMeta("UnicastPacketsDeltaMin", "unicastPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorEthPortMcastStats", "adaptorEthPortMcastStats", "eth-port-mcast-stats-[TrafficDirection]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [u'adaptorEthPortMcastStatsHist'], ["Get"], ["admin", "operations", "read-only"])
}

