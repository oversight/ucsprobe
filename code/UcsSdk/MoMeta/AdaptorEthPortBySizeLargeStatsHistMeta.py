import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"GreaterThanOrEqualTo9216":UcsPropertyMeta("GreaterThanOrEqualTo9216", "greaterThanOrEqualTo9216", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"GreaterThanOrEqualTo9216Delta":UcsPropertyMeta("GreaterThanOrEqualTo9216Delta", "greaterThanOrEqualTo9216Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"GreaterThanOrEqualTo9216DeltaAvg":UcsPropertyMeta("GreaterThanOrEqualTo9216DeltaAvg", "greaterThanOrEqualTo9216DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"GreaterThanOrEqualTo9216DeltaMax":UcsPropertyMeta("GreaterThanOrEqualTo9216DeltaMax", "greaterThanOrEqualTo9216DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"GreaterThanOrEqualTo9216DeltaMin":UcsPropertyMeta("GreaterThanOrEqualTo9216DeltaMin", "greaterThanOrEqualTo9216DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.Naming, None, None, None, None, [], ["0-4294967295"]),
	"LessThan2048":UcsPropertyMeta("LessThan2048", "lessThan2048", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan2048Delta":UcsPropertyMeta("LessThan2048Delta", "lessThan2048Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan2048DeltaAvg":UcsPropertyMeta("LessThan2048DeltaAvg", "lessThan2048DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan2048DeltaMax":UcsPropertyMeta("LessThan2048DeltaMax", "lessThan2048DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan2048DeltaMin":UcsPropertyMeta("LessThan2048DeltaMin", "lessThan2048DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan4096":UcsPropertyMeta("LessThan4096", "lessThan4096", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan4096Delta":UcsPropertyMeta("LessThan4096Delta", "lessThan4096Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan4096DeltaAvg":UcsPropertyMeta("LessThan4096DeltaAvg", "lessThan4096DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan4096DeltaMax":UcsPropertyMeta("LessThan4096DeltaMax", "lessThan4096DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan4096DeltaMin":UcsPropertyMeta("LessThan4096DeltaMin", "lessThan4096DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan8192":UcsPropertyMeta("LessThan8192", "lessThan8192", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan8192Delta":UcsPropertyMeta("LessThan8192Delta", "lessThan8192Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan8192DeltaAvg":UcsPropertyMeta("LessThan8192DeltaAvg", "lessThan8192DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan8192DeltaMax":UcsPropertyMeta("LessThan8192DeltaMax", "lessThan8192DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan8192DeltaMin":UcsPropertyMeta("LessThan8192DeltaMin", "lessThan8192DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan9216":UcsPropertyMeta("LessThan9216", "lessThan9216", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan9216Delta":UcsPropertyMeta("LessThan9216Delta", "lessThan9216Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan9216DeltaAvg":UcsPropertyMeta("LessThan9216DeltaAvg", "lessThan9216DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan9216DeltaMax":UcsPropertyMeta("LessThan9216DeltaMax", "lessThan9216DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThan9216DeltaMin":UcsPropertyMeta("LessThan9216DeltaMin", "lessThan9216DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThanOrEqualTo1518":UcsPropertyMeta("LessThanOrEqualTo1518", "lessThanOrEqualTo1518", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThanOrEqualTo1518Delta":UcsPropertyMeta("LessThanOrEqualTo1518Delta", "lessThanOrEqualTo1518Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThanOrEqualTo1518DeltaAvg":UcsPropertyMeta("LessThanOrEqualTo1518DeltaAvg", "lessThanOrEqualTo1518DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThanOrEqualTo1518DeltaMax":UcsPropertyMeta("LessThanOrEqualTo1518DeltaMax", "lessThanOrEqualTo1518DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LessThanOrEqualTo1518DeltaMin":UcsPropertyMeta("LessThanOrEqualTo1518DeltaMin", "lessThanOrEqualTo1518DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MostRecent":UcsPropertyMeta("MostRecent", "mostRecent", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"NoBreakdownGreaterThan1518":UcsPropertyMeta("NoBreakdownGreaterThan1518", "noBreakdownGreaterThan1518", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"NoBreakdownGreaterThan1518Delta":UcsPropertyMeta("NoBreakdownGreaterThan1518Delta", "noBreakdownGreaterThan1518Delta", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"NoBreakdownGreaterThan1518DeltaAvg":UcsPropertyMeta("NoBreakdownGreaterThan1518DeltaAvg", "noBreakdownGreaterThan1518DeltaAvg", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"NoBreakdownGreaterThan1518DeltaMax":UcsPropertyMeta("NoBreakdownGreaterThan1518DeltaMax", "noBreakdownGreaterThan1518DeltaMax", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"NoBreakdownGreaterThan1518DeltaMin":UcsPropertyMeta("NoBreakdownGreaterThan1518DeltaMin", "noBreakdownGreaterThan1518DeltaMin", "ulong", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Suspect":UcsPropertyMeta("Suspect", "suspect", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Thresholded":UcsPropertyMeta("Thresholded", "thresholded", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"TimeCollected":UcsPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorEthPortBySizeLargeStatsHist", "adaptorEthPortBySizeLargeStatsHist", "[Id]", _VersionMeta.Version111j, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"])
}

