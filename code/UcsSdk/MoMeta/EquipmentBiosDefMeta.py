import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version202m, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version202m, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"ResetOn":UcsPropertyMeta("ResetOn", "resetOn", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["Activate", "Unknown", "Update"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"SecureBios":UcsPropertyMeta("SecureBios", "secureBios", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["Not supported", "Supported", "Unknown"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"StorageMethod":UcsPropertyMeta("StorageMethod", "storageMethod", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["Dual Flash", "Single Flash", "Unknown"], ["0-4294967295"]),
	"UpdateMethod":UcsPropertyMeta("UpdateMethod", "updateMethod", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["Management Controller", "Pnuos", "Unknown"], ["0-4294967295"]),
	"Meta":UcsMoMeta("EquipmentBiosDef", "equipmentBiosDef", "bios-def", _VersionMeta.Version202m, "InputOutput", 0x7fL, [], [], ["Get"], [""])
}

