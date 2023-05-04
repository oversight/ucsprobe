import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Authorization":UcsPropertyMeta("Authorization", "authorization", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["disable", "enable"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"TargetAttr":UcsPropertyMeta("TargetAttr", "targetAttr", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x80L, 0, 63, None, [], ["0-4294967295"]),
	"Traversal":UcsPropertyMeta("Traversal", "traversal", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["non-recursive", "recursive"], ["0-4294967295"]),
	"UsePrimaryGroup":UcsPropertyMeta("UsePrimaryGroup", "usePrimaryGroup", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Meta":UcsMoMeta("AaaLdapGroupRule", "aaaLdapGroupRule", "ldapgroup-rule", _VersionMeta.Version141i, "InputOutput", 0x3ffL, [], [], ["Add", "Get", "Remove", "Set"], ["aaa", "admin"])
}

