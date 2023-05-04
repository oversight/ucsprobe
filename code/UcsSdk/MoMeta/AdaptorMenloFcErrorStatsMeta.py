import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"CorrectableErrors":UcsPropertyMeta("CorrectableErrors", "correctableErrors", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"CorrectableErrorsDelta":UcsPropertyMeta("CorrectableErrorsDelta", "correctableErrorsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"CorrectableErrorsDeltaAvg":UcsPropertyMeta("CorrectableErrorsDeltaAvg", "correctableErrorsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"CorrectableErrorsDeltaMax":UcsPropertyMeta("CorrectableErrorsDeltaMax", "correctableErrorsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"CorrectableErrorsDeltaMin":UcsPropertyMeta("CorrectableErrorsDeltaMin", "correctableErrorsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MenloFcIndex":UcsPropertyMeta("MenloFcIndex", "menloFcIndex", "string", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, ["0", "0_A", "0_B", "1", "1_A", "1_B", "unknown"], ["0-4294967295"]),
	"PopErrors":UcsPropertyMeta("PopErrors", "popErrors", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PopErrorsDelta":UcsPropertyMeta("PopErrorsDelta", "popErrorsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PopErrorsDeltaAvg":UcsPropertyMeta("PopErrorsDeltaAvg", "popErrorsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PopErrorsDeltaMax":UcsPropertyMeta("PopErrorsDeltaMax", "popErrorsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PopErrorsDeltaMin":UcsPropertyMeta("PopErrorsDeltaMin", "popErrorsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PushErrors":UcsPropertyMeta("PushErrors", "pushErrors", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PushErrorsDelta":UcsPropertyMeta("PushErrorsDelta", "pushErrorsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PushErrorsDeltaAvg":UcsPropertyMeta("PushErrorsDeltaAvg", "pushErrorsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PushErrorsDeltaMax":UcsPropertyMeta("PushErrorsDeltaMax", "pushErrorsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PushErrorsDeltaMin":UcsPropertyMeta("PushErrorsDeltaMin", "pushErrorsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"UncorrectableErrors":UcsPropertyMeta("UncorrectableErrors", "uncorrectableErrors", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UncorrectableErrorsDelta":UcsPropertyMeta("UncorrectableErrorsDelta", "uncorrectableErrorsDelta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UncorrectableErrorsDeltaAvg":UcsPropertyMeta("UncorrectableErrorsDeltaAvg", "uncorrectableErrorsDeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UncorrectableErrorsDeltaMax":UcsPropertyMeta("UncorrectableErrorsDeltaMax", "uncorrectableErrorsDeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"UncorrectableErrorsDeltaMin":UcsPropertyMeta("UncorrectableErrorsDeltaMin", "uncorrectableErrorsDeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorMenloFcErrorStats", "adaptorMenloFcErrorStats", "menlo-fc-error-stats-[MenloFcIndex]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [u'adaptorMenloFcErrorStatsHist'], ["Get"], ["admin", "operations", "read-only"])
}

