import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConfigState":UcsPropertyMeta("ConfigState", "configState", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applied", "ok"], ["0-4294967295"]),
	"ConfigStatusMessage":UcsPropertyMeta("ConfigStatusMessage", "configStatusMessage", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Domain":UcsPropertyMeta("Domain", "domain", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[a-zA-Z][a-zA-Z0-9@_.\-\\]{0,47}""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x10L, None, None, """[a-zA-Z][a-zA-Z0-9@_.\-\\]{0,47}""", [], ["0-4294967295"]),
	"Priv":UcsPropertyMeta("Priv", "priv", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["admin", "readonly"], ["0-4294967295"]),
	"Pwd":UcsPropertyMeta("Pwd", "pwd", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{1,20}""", [], ["0-4294967295"]),
	"PwdSet":UcsPropertyMeta("PwdSet", "pwdSet", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("StorageEpUser", "storageEpUser", "user-[Name]", _VersionMeta.Version211a, "InputOutput", 0x1ffL, [], [u'aaaCimcSession'], [None], ["admin"])
}

