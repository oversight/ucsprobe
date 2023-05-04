import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"BadCrcPackets":UcsPropertyMeta("BadCrcPackets", "badCrcPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BadCrcPacketsDelta":UcsPropertyMeta("BadCrcPacketsDelta", "badCrcPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BadCrcPacketsDeltaAvg":UcsPropertyMeta("BadCrcPacketsDeltaAvg", "badCrcPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BadCrcPacketsDeltaMax":UcsPropertyMeta("BadCrcPacketsDeltaMax", "badCrcPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BadCrcPacketsDeltaMin":UcsPropertyMeta("BadCrcPacketsDeltaMin", "badCrcPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BadLengthPackets":UcsPropertyMeta("BadLengthPackets", "badLengthPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BadLengthPacketsDelta":UcsPropertyMeta("BadLengthPacketsDelta", "badLengthPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BadLengthPacketsDeltaAvg":UcsPropertyMeta("BadLengthPacketsDeltaAvg", "badLengthPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BadLengthPacketsDeltaMax":UcsPropertyMeta("BadLengthPacketsDeltaMax", "badLengthPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"BadLengthPacketsDeltaMin":UcsPropertyMeta("BadLengthPacketsDeltaMin", "badLengthPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, [], ["0-4294967295"]),
	"MacDiscardedPackets":UcsPropertyMeta("MacDiscardedPackets", "macDiscardedPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MacDiscardedPacketsDelta":UcsPropertyMeta("MacDiscardedPacketsDelta", "macDiscardedPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MacDiscardedPacketsDeltaAvg":UcsPropertyMeta("MacDiscardedPacketsDeltaAvg", "macDiscardedPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MacDiscardedPacketsDeltaMax":UcsPropertyMeta("MacDiscardedPacketsDeltaMax", "macDiscardedPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MacDiscardedPacketsDeltaMin":UcsPropertyMeta("MacDiscardedPacketsDeltaMin", "macDiscardedPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MostRecent":UcsPropertyMeta("MostRecent", "mostRecent", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorEthPortErrStatsHist", "adaptorEthPortErrStatsHist", "[Id]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"])
}

