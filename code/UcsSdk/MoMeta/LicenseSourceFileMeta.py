import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Exp":UcsPropertyMeta("Exp", "exp", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], ["0-4294967295"]),
	"HostId":UcsPropertyMeta("HostId", "hostId", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "string", _VersionMeta.Version141i, UcsPropertyMeta.Naming, 0x4L, 1, 32, None, [], ["0-4294967295"]),
	"Line":UcsPropertyMeta("Line", "line", "string", _VersionMeta.Version141i, UcsPropertyMeta.Naming, 0x8L, 1, 510, None, [], ["0-4294967295"]),
	"Pak":UcsPropertyMeta("Pak", "pak", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Quant":UcsPropertyMeta("Quant", "quant", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Sig":UcsPropertyMeta("Sig", "sig", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["feature", "increment", "upgrade"], ["0-4294967295"]),
	"Meta":UcsMoMeta("LicenseSourceFile", "licenseSourceFile", "src-[Id]:[Line]", _VersionMeta.Version141i, "InputOutput", 0x3fL, [], [], ["Get"], ["read-only"])
}

