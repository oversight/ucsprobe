import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"DropOverrunN0":UcsPropertyMeta("DropOverrunN0", "dropOverrunN0", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropOverrunN0Delta":UcsPropertyMeta("DropOverrunN0Delta", "dropOverrunN0Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropOverrunN0DeltaAvg":UcsPropertyMeta("DropOverrunN0DeltaAvg", "dropOverrunN0DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropOverrunN0DeltaMax":UcsPropertyMeta("DropOverrunN0DeltaMax", "dropOverrunN0DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropOverrunN0DeltaMin":UcsPropertyMeta("DropOverrunN0DeltaMin", "dropOverrunN0DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropOverrunN1":UcsPropertyMeta("DropOverrunN1", "dropOverrunN1", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropOverrunN1Delta":UcsPropertyMeta("DropOverrunN1Delta", "dropOverrunN1Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropOverrunN1DeltaAvg":UcsPropertyMeta("DropOverrunN1DeltaAvg", "dropOverrunN1DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropOverrunN1DeltaMax":UcsPropertyMeta("DropOverrunN1DeltaMax", "dropOverrunN1DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"DropOverrunN1DeltaMin":UcsPropertyMeta("DropOverrunN1DeltaMin", "dropOverrunN1DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Intervals":UcsPropertyMeta("Intervals", "intervals", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MenloQueueComponent":UcsPropertyMeta("MenloQueueComponent", "menloQueueComponent", "string", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, ["N", "cpu", "eth", "fc", "unknown"], ["0-4294967295"]),
	"MenloQueueIndex":UcsPropertyMeta("MenloQueueIndex", "menloQueueIndex", "string", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, ["0", "0_A", "0_B", "1", "1_A", "1_B", "unknown"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"TruncateOverrunN0":UcsPropertyMeta("TruncateOverrunN0", "truncateOverrunN0", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TruncateOverrunN0Delta":UcsPropertyMeta("TruncateOverrunN0Delta", "truncateOverrunN0Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TruncateOverrunN0DeltaAvg":UcsPropertyMeta("TruncateOverrunN0DeltaAvg", "truncateOverrunN0DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TruncateOverrunN0DeltaMax":UcsPropertyMeta("TruncateOverrunN0DeltaMax", "truncateOverrunN0DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TruncateOverrunN0DeltaMin":UcsPropertyMeta("TruncateOverrunN0DeltaMin", "truncateOverrunN0DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TruncateOverrunN1":UcsPropertyMeta("TruncateOverrunN1", "truncateOverrunN1", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TruncateOverrunN1Delta":UcsPropertyMeta("TruncateOverrunN1Delta", "truncateOverrunN1Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TruncateOverrunN1DeltaAvg":UcsPropertyMeta("TruncateOverrunN1DeltaAvg", "truncateOverrunN1DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TruncateOverrunN1DeltaMax":UcsPropertyMeta("TruncateOverrunN1DeltaMax", "truncateOverrunN1DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TruncateOverrunN1DeltaMin":UcsPropertyMeta("TruncateOverrunN1DeltaMin", "truncateOverrunN1DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Update":UcsPropertyMeta("Update", "update", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorMenloQStats", "adaptorMenloQStats", "menlo-q-stats-comp-[MenloQueueComponent]index-[MenloQueueIndex]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [u'adaptorMenloQStatsHist'], ["Get"], ["admin", "operations", "read-only"])
}

