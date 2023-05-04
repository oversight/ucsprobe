import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MenloPortIndex":UcsPropertyMeta("MenloPortIndex", "menloPortIndex", "string", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, ["0", "0_A", "0_B", "1", "1_A", "1_B", "unknown"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"RxPauseCFC":UcsPropertyMeta("RxPauseCFC", "rxPauseCFC", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RxPauseCFCDelta":UcsPropertyMeta("RxPauseCFCDelta", "rxPauseCFCDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RxPauseCFCDeltaAvg":UcsPropertyMeta("RxPauseCFCDeltaAvg", "rxPauseCFCDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RxPauseCFCDeltaMax":UcsPropertyMeta("RxPauseCFCDeltaMax", "rxPauseCFCDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RxPauseCFCDeltaMin":UcsPropertyMeta("RxPauseCFCDeltaMin", "rxPauseCFCDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RxPausePFC":UcsPropertyMeta("RxPausePFC", "rxPausePFC", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RxPausePFCDelta":UcsPropertyMeta("RxPausePFCDelta", "rxPausePFCDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RxPausePFCDeltaAvg":UcsPropertyMeta("RxPausePFCDeltaAvg", "rxPausePFCDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RxPausePFCDeltaMax":UcsPropertyMeta("RxPausePFCDeltaMax", "rxPausePFCDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RxPausePFCDeltaMin":UcsPropertyMeta("RxPausePFCDeltaMin", "rxPausePFCDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"TxPauseCFC":UcsPropertyMeta("TxPauseCFC", "txPauseCFC", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TxPauseCFCDelta":UcsPropertyMeta("TxPauseCFCDelta", "txPauseCFCDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TxPauseCFCDeltaAvg":UcsPropertyMeta("TxPauseCFCDeltaAvg", "txPauseCFCDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TxPauseCFCDeltaMax":UcsPropertyMeta("TxPauseCFCDeltaMax", "txPauseCFCDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TxPauseCFCDeltaMin":UcsPropertyMeta("TxPauseCFCDeltaMin", "txPauseCFCDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TxPausePFC":UcsPropertyMeta("TxPausePFC", "txPausePFC", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TxPausePFCDelta":UcsPropertyMeta("TxPausePFCDelta", "txPausePFCDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TxPausePFCDeltaAvg":UcsPropertyMeta("TxPausePFCDeltaAvg", "txPausePFCDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TxPausePFCDeltaMax":UcsPropertyMeta("TxPausePFCDeltaMax", "txPausePFCDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TxPausePFCDeltaMin":UcsPropertyMeta("TxPausePFCDeltaMin", "txPausePFCDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorMenloDcePortStats", "adaptorMenloDcePortStats", "menlo-dce-port-stats-[MenloPortIndex]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [u'adaptorMenloDcePortStatsHist'], ["Get"], ["admin", "operations", "read-only"])
}

