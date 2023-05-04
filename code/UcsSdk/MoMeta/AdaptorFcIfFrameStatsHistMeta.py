import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"DumpedFrames":UcsPropertyMeta("DumpedFrames", "dumpedFrames", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"DumpedFramesDelta":UcsPropertyMeta("DumpedFramesDelta", "dumpedFramesDelta", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"DumpedFramesDeltaAvg":UcsPropertyMeta("DumpedFramesDeltaAvg", "dumpedFramesDeltaAvg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"DumpedFramesDeltaMax":UcsPropertyMeta("DumpedFramesDeltaMax", "dumpedFramesDeltaMax", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"DumpedFramesDeltaMin":UcsPropertyMeta("DumpedFramesDeltaMin", "dumpedFramesDeltaMin", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"ErrorFrames":UcsPropertyMeta("ErrorFrames", "errorFrames", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"ErrorFramesDelta":UcsPropertyMeta("ErrorFramesDelta", "errorFramesDelta", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"ErrorFramesDeltaAvg":UcsPropertyMeta("ErrorFramesDeltaAvg", "errorFramesDeltaAvg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"ErrorFramesDeltaMax":UcsPropertyMeta("ErrorFramesDeltaMax", "errorFramesDeltaMax", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"ErrorFramesDeltaMin":UcsPropertyMeta("ErrorFramesDeltaMin", "errorFramesDeltaMin", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, [], ["0-4294967295"]),
	"MostRecent":UcsPropertyMeta("MostRecent", "mostRecent", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"RxFrames":UcsPropertyMeta("RxFrames", "rxFrames", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"RxFramesDelta":UcsPropertyMeta("RxFramesDelta", "rxFramesDelta", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"RxFramesDeltaAvg":UcsPropertyMeta("RxFramesDeltaAvg", "rxFramesDeltaAvg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"RxFramesDeltaMax":UcsPropertyMeta("RxFramesDeltaMax", "rxFramesDeltaMax", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"RxFramesDeltaMin":UcsPropertyMeta("RxFramesDeltaMin", "rxFramesDeltaMin", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"TxFrames":UcsPropertyMeta("TxFrames", "txFrames", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"TxFramesDelta":UcsPropertyMeta("TxFramesDelta", "txFramesDelta", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"TxFramesDeltaAvg":UcsPropertyMeta("TxFramesDeltaAvg", "txFramesDeltaAvg", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"TxFramesDeltaMax":UcsPropertyMeta("TxFramesDeltaMax", "txFramesDeltaMax", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"TxFramesDeltaMin":UcsPropertyMeta("TxFramesDeltaMin", "txFramesDeltaMin", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["NA"], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorFcIfFrameStatsHist", "adaptorFcIfFrameStatsHist", "[Id]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"])
}

