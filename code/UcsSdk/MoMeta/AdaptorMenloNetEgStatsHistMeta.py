import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"DropCmd":UcsPropertyMeta("DropCmd", "dropCmd", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropCmdDelta":UcsPropertyMeta("DropCmdDelta", "dropCmdDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropCmdDeltaAvg":UcsPropertyMeta("DropCmdDeltaAvg", "dropCmdDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropCmdDeltaMax":UcsPropertyMeta("DropCmdDeltaMax", "dropCmdDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropCmdDeltaMin":UcsPropertyMeta("DropCmdDeltaMin", "dropCmdDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropLifCfgInvalid":UcsPropertyMeta("DropLifCfgInvalid", "dropLifCfgInvalid", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropLifCfgInvalidDelta":UcsPropertyMeta("DropLifCfgInvalidDelta", "dropLifCfgInvalidDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropLifCfgInvalidDeltaAvg":UcsPropertyMeta("DropLifCfgInvalidDeltaAvg", "dropLifCfgInvalidDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropLifCfgInvalidDeltaMax":UcsPropertyMeta("DropLifCfgInvalidDeltaMax", "dropLifCfgInvalidDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropLifCfgInvalidDeltaMin":UcsPropertyMeta("DropLifCfgInvalidDeltaMin", "dropLifCfgInvalidDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropLifMapNoHit":UcsPropertyMeta("DropLifMapNoHit", "dropLifMapNoHit", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropLifMapNoHitDelta":UcsPropertyMeta("DropLifMapNoHitDelta", "dropLifMapNoHitDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropLifMapNoHitDeltaAvg":UcsPropertyMeta("DropLifMapNoHitDeltaAvg", "dropLifMapNoHitDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropLifMapNoHitDeltaMax":UcsPropertyMeta("DropLifMapNoHitDeltaMax", "dropLifMapNoHitDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropLifMapNoHitDeltaMin":UcsPropertyMeta("DropLifMapNoHitDeltaMin", "dropLifMapNoHitDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropSrcBind":UcsPropertyMeta("DropSrcBind", "dropSrcBind", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropSrcBindDelta":UcsPropertyMeta("DropSrcBindDelta", "dropSrcBindDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropSrcBindDeltaAvg":UcsPropertyMeta("DropSrcBindDeltaAvg", "dropSrcBindDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropSrcBindDeltaMax":UcsPropertyMeta("DropSrcBindDeltaMax", "dropSrcBindDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropSrcBindDeltaMin":UcsPropertyMeta("DropSrcBindDeltaMin", "dropSrcBindDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, [], ["0-4294967295"]),
	"LearnReqDrop":UcsPropertyMeta("LearnReqDrop", "learnReqDrop", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LearnReqDropDelta":UcsPropertyMeta("LearnReqDropDelta", "learnReqDropDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LearnReqDropDeltaAvg":UcsPropertyMeta("LearnReqDropDeltaAvg", "learnReqDropDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LearnReqDropDeltaMax":UcsPropertyMeta("LearnReqDropDeltaMax", "learnReqDropDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LearnReqDropDeltaMin":UcsPropertyMeta("LearnReqDropDeltaMin", "learnReqDropDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MostRecent":UcsPropertyMeta("MostRecent", "mostRecent", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorMenloNetEgStatsHist", "adaptorMenloNetEgStatsHist", "[Id]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"])
}

