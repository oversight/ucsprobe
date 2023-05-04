import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Burst":UcsPropertyMeta("Burst", "burst", "uint", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, [], ["0-65535"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"HostControl":UcsPropertyMeta("HostControl", "hostControl", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, ["full", "full-with-exception", "none"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"OperPrio":UcsPropertyMeta("OperPrio", "operPrio", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["best-effort", "bronze", "fc", "gold", "platinum", "silver"], ["0-4294967295"]),
	"Prio":UcsPropertyMeta("Prio", "prio", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["best-effort", "bronze", "fc", "gold", "platinum", "silver"], ["0-4294967295"]),
	"Rate":UcsPropertyMeta("Rate", "rate", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["line-rate"], ["8-40000000"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EpqosEgress", "epqosEgress", "egress", _VersionMeta.Version101e, "InputOutput", 0x1ffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "ls-network", "ls-network-policy", "ls-qos-policy", "read-only"])
}

