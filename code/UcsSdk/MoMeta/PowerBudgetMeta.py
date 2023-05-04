import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminCommitted":UcsPropertyMeta("AdminCommitted", "adminCommitted", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
	"AdminPeak":UcsPropertyMeta("AdminPeak", "adminPeak", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
	"CapAction":UcsPropertyMeta("CapAction", "capAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["clock-down", "nothing", "throttled"], ["0-4294967295"]),
	"CatalogPower":UcsPropertyMeta("CatalogPower", "catalogPower", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"CurrentPower":UcsPropertyMeta("CurrentPower", "currentPower", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"DynRealloc":UcsPropertyMeta("DynRealloc", "dynRealloc", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["chassis", "none"], ["0-4294967295"]),
	"GroupName":UcsPropertyMeta("GroupName", "groupName", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"IdlePower":UcsPropertyMeta("IdlePower", "idlePower", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
	"MaxPower":UcsPropertyMeta("MaxPower", "maxPower", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
	"MinPower":UcsPropertyMeta("MinPower", "minPower", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
	"OperCommitted":UcsPropertyMeta("OperCommitted", "operCommitted", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
	"OperMin":UcsPropertyMeta("OperMin", "operMin", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
	"OperPeak":UcsPropertyMeta("OperPeak", "operPeak", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unbounded"], ["0-10000000", "4294967295-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["budgeted", "budgeting", "deployed", "deploying", "discovery-retry", "firmware-mismatch", "non-compliant", "not-capped"], ["0-4294967295"]),
	"Prio":UcsPropertyMeta("Prio", "prio", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["no-cap", "utility"], ["1-10"]),
	"PsuCapacity":UcsPropertyMeta("PsuCapacity", "psuCapacity", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-20000"]),
	"PsuState":UcsPropertyMeta("PsuState", "psuState", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["insufficient", "ok"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"ScaledWt":UcsPropertyMeta("ScaledWt", "scaledWt", "byte", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-200"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Style":UcsPropertyMeta("Style", "style", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["intelligent-policy-driven", "manual-per-blade"], ["0-4294967295"]),
	"UpdateTime":UcsPropertyMeta("UpdateTime", "updateTime", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Weight":UcsPropertyMeta("Weight", "weight", "byte", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-200"]),
	"Meta":UcsMoMeta("PowerBudget", "powerBudget", "budget", _VersionMeta.Version111j, "InputOutput", 0x1fL, [], [u'faultInst'], ["Get"], ["admin", "power-mgmt"])
}

