import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, [], ["0-4294967295"]),
	"MostRecent":UcsPropertyMeta("MostRecent", "mostRecent", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"OversizedBadCrcPackets":UcsPropertyMeta("OversizedBadCrcPackets", "oversizedBadCrcPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedBadCrcPacketsDelta":UcsPropertyMeta("OversizedBadCrcPacketsDelta", "oversizedBadCrcPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedBadCrcPacketsDeltaAvg":UcsPropertyMeta("OversizedBadCrcPacketsDeltaAvg", "oversizedBadCrcPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedBadCrcPacketsDeltaMax":UcsPropertyMeta("OversizedBadCrcPacketsDeltaMax", "oversizedBadCrcPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedBadCrcPacketsDeltaMin":UcsPropertyMeta("OversizedBadCrcPacketsDeltaMin", "oversizedBadCrcPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedGoodCrcPackets":UcsPropertyMeta("OversizedGoodCrcPackets", "oversizedGoodCrcPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedGoodCrcPacketsDelta":UcsPropertyMeta("OversizedGoodCrcPacketsDelta", "oversizedGoodCrcPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedGoodCrcPacketsDeltaAvg":UcsPropertyMeta("OversizedGoodCrcPacketsDeltaAvg", "oversizedGoodCrcPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedGoodCrcPacketsDeltaMax":UcsPropertyMeta("OversizedGoodCrcPacketsDeltaMax", "oversizedGoodCrcPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedGoodCrcPacketsDeltaMin":UcsPropertyMeta("OversizedGoodCrcPacketsDeltaMin", "oversizedGoodCrcPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedPackets":UcsPropertyMeta("OversizedPackets", "oversizedPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedPacketsDelta":UcsPropertyMeta("OversizedPacketsDelta", "oversizedPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedPacketsDeltaAvg":UcsPropertyMeta("OversizedPacketsDeltaAvg", "oversizedPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedPacketsDeltaMax":UcsPropertyMeta("OversizedPacketsDeltaMax", "oversizedPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OversizedPacketsDeltaMin":UcsPropertyMeta("OversizedPacketsDeltaMin", "oversizedPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"UndersizedBadCrcPackets":UcsPropertyMeta("UndersizedBadCrcPackets", "undersizedBadCrcPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UndersizedBadCrcPacketsDelta":UcsPropertyMeta("UndersizedBadCrcPacketsDelta", "undersizedBadCrcPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UndersizedBadCrcPacketsDeltaAvg":UcsPropertyMeta("UndersizedBadCrcPacketsDeltaAvg", "undersizedBadCrcPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UndersizedBadCrcPacketsDeltaMax":UcsPropertyMeta("UndersizedBadCrcPacketsDeltaMax", "undersizedBadCrcPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UndersizedBadCrcPacketsDeltaMin":UcsPropertyMeta("UndersizedBadCrcPacketsDeltaMin", "undersizedBadCrcPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UndersizedGoodCrcPackets":UcsPropertyMeta("UndersizedGoodCrcPackets", "undersizedGoodCrcPackets", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UndersizedGoodCrcPacketsDelta":UcsPropertyMeta("UndersizedGoodCrcPacketsDelta", "undersizedGoodCrcPacketsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UndersizedGoodCrcPacketsDeltaAvg":UcsPropertyMeta("UndersizedGoodCrcPacketsDeltaAvg", "undersizedGoodCrcPacketsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UndersizedGoodCrcPacketsDeltaMax":UcsPropertyMeta("UndersizedGoodCrcPacketsDeltaMax", "undersizedGoodCrcPacketsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UndersizedGoodCrcPacketsDeltaMin":UcsPropertyMeta("UndersizedGoodCrcPacketsDeltaMin", "undersizedGoodCrcPacketsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorEthPortOutsizedStatsHist", "adaptorEthPortOutsizedStatsHist", "[Id]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"])
}

