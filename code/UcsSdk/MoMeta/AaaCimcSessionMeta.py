import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["active", "inactive"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version212a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"CimcAddr":UcsPropertyMeta("CimcAddr", "cimcAddr", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "string", _VersionMeta.Version212a, UcsPropertyMeta.Naming, 0x4L, 1, 32, None, [], ["0-4294967295"]),
	"IntDel":UcsPropertyMeta("IntDel", "intDel", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"IsDelete":UcsPropertyMeta("IsDelete", "isDelete", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, ["no", "yes"], ["0-4294967295"]),
	"LastUpdatedTime":UcsPropertyMeta("LastUpdatedTime", "lastUpdatedTime", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"LoginTime":UcsPropertyMeta("LoginTime", "loginTime", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"LsDn":UcsPropertyMeta("LsDn", "lsDn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Pid":UcsPropertyMeta("Pid", "pid", "uint", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PnDn":UcsPropertyMeta("PnDn", "pnDn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Priv":UcsPropertyMeta("Priv", "priv", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"SourceAddr":UcsPropertyMeta("SourceAddr", "sourceAddr", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["all", "kvm", "sol", "vmedia"], ["0-4294967295"]),
	"User":UcsPropertyMeta("User", "user", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AaaCimcSession", "aaaCimcSession", "cimc-term-[Id]", _VersionMeta.Version212a, "InputOutput", 0x3fL, [], [], ["Get", "Set"], ["admin"])
}

