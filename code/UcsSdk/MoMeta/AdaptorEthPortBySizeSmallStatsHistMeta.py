import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Equals64":UcsPropertyMeta("Equals64", "equals64", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Equals64Delta":UcsPropertyMeta("Equals64Delta", "equals64Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Equals64DeltaAvg":UcsPropertyMeta("Equals64DeltaAvg", "equals64DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Equals64DeltaMax":UcsPropertyMeta("Equals64DeltaMax", "equals64DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Equals64DeltaMin":UcsPropertyMeta("Equals64DeltaMin", "equals64DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, [], ["0-4294967295"]),
	"LessThan1024":UcsPropertyMeta("LessThan1024", "lessThan1024", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan1024Delta":UcsPropertyMeta("LessThan1024Delta", "lessThan1024Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan1024DeltaAvg":UcsPropertyMeta("LessThan1024DeltaAvg", "lessThan1024DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan1024DeltaMax":UcsPropertyMeta("LessThan1024DeltaMax", "lessThan1024DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan1024DeltaMin":UcsPropertyMeta("LessThan1024DeltaMin", "lessThan1024DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan128":UcsPropertyMeta("LessThan128", "lessThan128", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan128Delta":UcsPropertyMeta("LessThan128Delta", "lessThan128Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan128DeltaAvg":UcsPropertyMeta("LessThan128DeltaAvg", "lessThan128DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan128DeltaMax":UcsPropertyMeta("LessThan128DeltaMax", "lessThan128DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan128DeltaMin":UcsPropertyMeta("LessThan128DeltaMin", "lessThan128DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan256":UcsPropertyMeta("LessThan256", "lessThan256", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan256Delta":UcsPropertyMeta("LessThan256Delta", "lessThan256Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan256DeltaAvg":UcsPropertyMeta("LessThan256DeltaAvg", "lessThan256DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan256DeltaMax":UcsPropertyMeta("LessThan256DeltaMax", "lessThan256DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan256DeltaMin":UcsPropertyMeta("LessThan256DeltaMin", "lessThan256DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan512":UcsPropertyMeta("LessThan512", "lessThan512", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan512Delta":UcsPropertyMeta("LessThan512Delta", "lessThan512Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan512DeltaAvg":UcsPropertyMeta("LessThan512DeltaAvg", "lessThan512DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan512DeltaMax":UcsPropertyMeta("LessThan512DeltaMax", "lessThan512DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan512DeltaMin":UcsPropertyMeta("LessThan512DeltaMin", "lessThan512DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan64":UcsPropertyMeta("LessThan64", "lessThan64", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan64Delta":UcsPropertyMeta("LessThan64Delta", "lessThan64Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan64DeltaAvg":UcsPropertyMeta("LessThan64DeltaAvg", "lessThan64DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan64DeltaMax":UcsPropertyMeta("LessThan64DeltaMax", "lessThan64DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan64DeltaMin":UcsPropertyMeta("LessThan64DeltaMin", "lessThan64DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MostRecent":UcsPropertyMeta("MostRecent", "mostRecent", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorEthPortBySizeSmallStatsHist", "adaptorEthPortBySizeSmallStatsHist", "[Id]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"])
}

