import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AccountStatus":UcsPropertyMeta("AccountStatus", "accountStatus", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["active", "inactive"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ClearPwdHistory":UcsPropertyMeta("ClearPwdHistory", "clearPwdHistory", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["no", "yes"], ["0-4294967295"]),
	"ConfigState":UcsPropertyMeta("ConfigState", "configState", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applied", "ok"], ["0-4294967295"]),
	"ConfigStatusMessage":UcsPropertyMeta("ConfigStatusMessage", "configStatusMessage", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Email":UcsPropertyMeta("Email", "email", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, 0, 510, None, [], ["0-4294967295"]),
	"EncPwd":UcsPropertyMeta("EncPwd", "encPwd", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"EncPwdSet":UcsPropertyMeta("EncPwdSet", "encPwdSet", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Expiration":UcsPropertyMeta("Expiration", "expiration", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], ["0-4294967295"]),
	"Expires":UcsPropertyMeta("Expires", "expires", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"FirstName":UcsPropertyMeta("FirstName", "firstName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, 0, 32, None, [], ["0-4294967295"]),
	"LastName":UcsPropertyMeta("LastName", "lastName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, 0, 32, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x1000L, None, None, """[a-zA-Z][a-zA-Z0-9_.-]{0,31}""", [], ["0-4294967295"]),
	"Phone":UcsPropertyMeta("Phone", "phone", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2000L, 0, 510, None, [], ["0-4294967295"]),
	"Priv":UcsPropertyMeta("Priv", "priv", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """((ext-lan-policy|pn-maintenance|ls-security-policy|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|operations|ext-lan-config|pn-security|ls-network-policy|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault),){0,37}(ext-lan-policy|pn-maintenance|ls-security-policy|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|operations|ext-lan-config|pn-security|ls-network-policy|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault){0,1}""", [], ["0-4294967295"]),
	"Pwd":UcsPropertyMeta("Pwd", "pwd", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4000L, None, None, """[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,80}""", [], ["0-4294967295"]),
	"PwdLifeTime":UcsPropertyMeta("PwdLifeTime", "pwdLifeTime", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x8000L, None, None, None, ["no-password-expire"], ["0-3650"]),
	"PwdSet":UcsPropertyMeta("PwdSet", "pwdSet", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10000L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AaaUser", "aaaUser", "user-[Name]", _VersionMeta.Version101e, "InputOutput", 0x3ffffL, [], [u'aaaCimcSession', u'aaaSession', u'aaaSshAuth', u'aaaUserData', u'aaaUserLocale', u'aaaUserRole', u'faultInst'], ["Add", "Get", "Remove", "Set"], ["aaa", "admin"])
}

