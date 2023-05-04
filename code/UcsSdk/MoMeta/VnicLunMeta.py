import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Bootable":UcsPropertyMeta("Bootable", "bootable", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-65535"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("VnicLun", "vnicLun", "lun", _VersionMeta.Version201m, "InputOutput", 0x3fL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "ls-config", "ls-server", "ls-storage"])
}

