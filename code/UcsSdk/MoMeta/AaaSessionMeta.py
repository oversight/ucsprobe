import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Host":UcsPropertyMeta("Host", "host", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, 1, 32, None, [], ["0-4294967295"]),
	"IntDel":UcsPropertyMeta("IntDel", "intDel", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"LoginTime":UcsPropertyMeta("LoginTime", "loginTime", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
	"Pid":UcsPropertyMeta("Pid", "pid", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"RefreshPeriod":UcsPropertyMeta("RefreshPeriod", "refreshPeriod", "uint", _VersionMeta.Version203a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"SessionTimeout":UcsPropertyMeta("SessionTimeout", "sessionTimeout", "uint", _VersionMeta.Version203a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Term":UcsPropertyMeta("Term", "term", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 16, None, [], ["0-4294967295"]),
	"Ui":UcsPropertyMeta("Ui", "ui", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ep", "kvm", "none", "shell", "sol", "vmedia", "web"], ["0-4294967295"]),
	"User":UcsPropertyMeta("User", "user", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AaaSession", "aaaSession", "term-[Id]", _VersionMeta.Version101e, "InputOutput", 0x1fL, [], [], ["Get", "Remove"], ["aaa", "admin"])
}

