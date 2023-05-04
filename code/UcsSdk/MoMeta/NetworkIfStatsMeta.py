import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"In":UcsPropertyMeta("In", "in", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Out":UcsPropertyMeta("Out", "out", "ulong", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x10L, None, None, None, ["broadcast", "generic", "multicast", "total", "unicast"], ["0-4294967295"]),
	"Units":UcsPropertyMeta("Units", "units", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x20L, None, None, None, ["octets", "packets", "raw"], ["0-4294967295"]),
	"Meta":UcsMoMeta("NetworkIfStats", "networkIfStats", "if-stat-[Type]-[Units]", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [], ["Get"], ["read-only"])
}

