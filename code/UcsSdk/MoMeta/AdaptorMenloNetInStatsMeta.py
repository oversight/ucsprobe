import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"DropFcLifInvalid":UcsPropertyMeta("DropFcLifInvalid", "dropFcLifInvalid", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropFcLifInvalidDelta":UcsPropertyMeta("DropFcLifInvalidDelta", "dropFcLifInvalidDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropFcLifInvalidDeltaAvg":UcsPropertyMeta("DropFcLifInvalidDeltaAvg", "dropFcLifInvalidDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropFcLifInvalidDeltaMax":UcsPropertyMeta("DropFcLifInvalidDeltaMax", "dropFcLifInvalidDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropFcLifInvalidDeltaMin":UcsPropertyMeta("DropFcLifInvalidDeltaMin", "dropFcLifInvalidDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropFcMulticast":UcsPropertyMeta("DropFcMulticast", "dropFcMulticast", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropFcMulticastDelta":UcsPropertyMeta("DropFcMulticastDelta", "dropFcMulticastDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropFcMulticastDeltaAvg":UcsPropertyMeta("DropFcMulticastDeltaAvg", "dropFcMulticastDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropFcMulticastDeltaMax":UcsPropertyMeta("DropFcMulticastDeltaMax", "dropFcMulticastDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropFcMulticastDeltaMin":UcsPropertyMeta("DropFcMulticastDeltaMin", "dropFcMulticastDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropNullPif":UcsPropertyMeta("DropNullPif", "dropNullPif", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropNullPifDelta":UcsPropertyMeta("DropNullPifDelta", "dropNullPifDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropNullPifDeltaAvg":UcsPropertyMeta("DropNullPifDeltaAvg", "dropNullPifDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropNullPifDeltaMax":UcsPropertyMeta("DropNullPifDeltaMax", "dropNullPifDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropNullPifDeltaMin":UcsPropertyMeta("DropNullPifDeltaMin", "dropNullPifDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FwdLookupNoHit":UcsPropertyMeta("FwdLookupNoHit", "fwdLookupNoHit", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FwdLookupNoHitDelta":UcsPropertyMeta("FwdLookupNoHitDelta", "fwdLookupNoHitDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FwdLookupNoHitDeltaAvg":UcsPropertyMeta("FwdLookupNoHitDeltaAvg", "fwdLookupNoHitDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FwdLookupNoHitDeltaMax":UcsPropertyMeta("FwdLookupNoHitDeltaMax", "fwdLookupNoHitDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FwdLookupNoHitDeltaMin":UcsPropertyMeta("FwdLookupNoHitDeltaMin", "fwdLookupNoHitDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MenloNetIndex":UcsPropertyMeta("MenloNetIndex", "menloNetIndex", "string", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, ["0", "0_A", "0_B", "1", "1_A", "1_B", "unknown"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorMenloNetInStats", "adaptorMenloNetInStats", "menlo-net-in-stats-[MenloNetIndex]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [u'adaptorMenloNetInStatsHist'], ["Get"], ["admin", "operations", "read-only"])
}

