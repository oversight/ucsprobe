import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Auth":UcsPropertyMeta("Auth", "auth", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["md5", "sha"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConfigState":UcsPropertyMeta("ConfigState", "configState", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applied", "ok"], ["0-4294967295"]),
	"ConfigStatusMessage":UcsPropertyMeta("ConfigStatusMessage", "configStatusMessage", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x10L, None, None, """[a-zA-Z][a-zA-Z0-9_.@-]{0,31}""", [], ["0-4294967295"]),
	"PrivPwdSet":UcsPropertyMeta("PrivPwdSet", "privPwdSet", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Privpwd":UcsPropertyMeta("Privpwd", "privpwd", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,80}""", [], ["0-4294967295"]),
	"Pwd":UcsPropertyMeta("Pwd", "pwd", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,80}""", [], ["0-4294967295"]),
	"PwdSet":UcsPropertyMeta("PwdSet", "pwdSet", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"UseAes":UcsPropertyMeta("UseAes", "useAes", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Meta":UcsMoMeta("CommSnmpUser", "commSnmpUser", "snmpv3-user-[Name]", _VersionMeta.Version101e, "InputOutput", 0x3ffL, [], [u'aaaCimcSession', u'faultInst'], ["Add", "Get", "Remove", "Set"], ["aaa", "admin"])
}

