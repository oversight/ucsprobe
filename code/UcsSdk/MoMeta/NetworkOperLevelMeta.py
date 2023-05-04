import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version212a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"MaxPrimaryVlanCount":UcsPropertyMeta("MaxPrimaryVlanCount", "maxPrimaryVlanCount", "uint", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MaxSecVlanPerPrimaryVlanCount":UcsPropertyMeta("MaxSecVlanPerPrimaryVlanCount", "maxSecVlanPerPrimaryVlanCount", "uint", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MaxSecondaryVlanCount":UcsPropertyMeta("MaxSecondaryVlanCount", "maxSecondaryVlanCount", "uint", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PrimaryVlanCount":UcsPropertyMeta("PrimaryVlanCount", "primaryVlanCount", "uint", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PrimaryVlanCountStatus":UcsPropertyMeta("PrimaryVlanCountStatus", "primaryVlanCountStatus", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["above-limit", "within-limit"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"SecondaryVlanCount":UcsPropertyMeta("SecondaryVlanCount", "secondaryVlanCount", "uint", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"SecondaryVlanCountStatus":UcsPropertyMeta("SecondaryVlanCountStatus", "secondaryVlanCountStatus", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["above-limit", "within-limit"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("NetworkOperLevel", "networkOperLevel", "oper-level", _VersionMeta.Version212a, "InputOutput", 0xfL, [], [u'faultInst'], [None], ["admin", "ext-lan-config"])
}

