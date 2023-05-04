import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Asic":UcsPropertyMeta("Asic", "asic", "string", _VersionMeta.Version201m, UcsPropertyMeta.Naming, 0x1L, None, None, None, ["carmel", "gatos", "unknown"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"PortCapacity":UcsPropertyMeta("PortCapacity", "portCapacity", "uint", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwComplexCapacity":UcsPropertyMeta("SwComplexCapacity", "swComplexCapacity", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"VifCapacity":UcsPropertyMeta("VifCapacity", "vifCapacity", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EquipmentPortGroupSwComplexDef", "equipmentPortGroupSwComplexDef", "port-group-sw-complex-def[Asic]", _VersionMeta.Version201m, "InputOutput", 0xffL, [], [u'equipmentPortSwComplexRef'], ["Get"], [""])
}

