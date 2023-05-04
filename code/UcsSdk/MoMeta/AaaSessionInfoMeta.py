import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Address":UcsPropertyMeta("Address", "address", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x1L, 0, 510, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version212a, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"DestIp":UcsPropertyMeta("DestIp", "destIp", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x4L, 0, 510, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Etime":UcsPropertyMeta("Etime", "etime", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "string", _VersionMeta.Version212a, UcsPropertyMeta.Naming, 0x20L, 1, 510, None, [], ["0-4294967295"]),
	"Priv":UcsPropertyMeta("Priv", "priv", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x40L, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["all", "kvm", "sol", "vmedia"], ["0-4294967295"]),
	"User":UcsPropertyMeta("User", "user", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x400L, 0, 510, None, [], ["0-4294967295"]),
	"UserType":UcsPropertyMeta("UserType", "userType", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, ["ipmi", "local", "remote"], ["0-4294967295"]),
	"Meta":UcsMoMeta("AaaSessionInfo", "aaaSessionInfo", "term-[Id]", _VersionMeta.Version212a, "InputOutput", 0xfffL, [], [], [None], ["aaa", "admin"])
}

