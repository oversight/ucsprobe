import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChangeCount":UcsPropertyMeta("ChangeCount", "changeCount", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, [], ["0-10"]),
	"ChangeDuringInterval":UcsPropertyMeta("ChangeDuringInterval", "changeDuringInterval", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, ["disable", "enable"], ["0-4294967295"]),
	"ChangeInterval":UcsPropertyMeta("ChangeInterval", "changeInterval", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["1-745"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, 0x8L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"ExpirationWarnTime":UcsPropertyMeta("ExpirationWarnTime", "expirationWarnTime", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["0-30"]),
	"HistoryCount":UcsPropertyMeta("HistoryCount", "historyCount", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, [], ["0-15"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version201m, UcsPropertyMeta.CreateOnly, 0x100L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"NoChangeInterval":UcsPropertyMeta("NoChangeInterval", "noChangeInterval", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, [], ["1-745"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x800L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AaaPwdProfile", "aaaPwdProfile", "pwd-profile", _VersionMeta.Version201m, "InputOutput", 0x1fffL, [], [], ["Get", "Set"], ["aaa", "admin"])
}

