import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Attribute":UcsPropertyMeta("Attribute", "attribute", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x1L, 0, 63, None, [], ["0-4294967295"]),
	"Basedn":UcsPropertyMeta("Basedn", "basedn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x2L, 0, 255, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x4L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"EnableSSL":UcsPropertyMeta("EnableSSL", "enableSSL", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"EncKey":UcsPropertyMeta("EncKey", "encKey", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, 1, 127, None, [], ["0-4294967295"]),
	"Filter":UcsPropertyMeta("Filter", "filter", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x80L, 0, 127, None, [], ["0-4294967295"]),
	"Key":UcsPropertyMeta("Key", "key", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """[!""#$%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,127}""", [], ["0-4294967295"]),
	"KeySet":UcsPropertyMeta("KeySet", "keySet", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x200L, None, None, """^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], ["0-4294967295"]),
	"Order":UcsPropertyMeta("Order", "order", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, ["lowest-available"], ["0-16"]),
	"Port":UcsPropertyMeta("Port", "port", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, [], ["1-65535"]),
	"Retries":UcsPropertyMeta("Retries", "retries", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, None, [], ["0-5"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2000L, 0, 256, None, [], ["0-4294967295"]),
	"Rootdn":UcsPropertyMeta("Rootdn", "rootdn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4000L, 0, 255, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Timeout":UcsPropertyMeta("Timeout", "timeout", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x10000L, None, None, None, [], ["0-60"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x20000L, None, None, None, ["MS-AD", "OpenLdap"], ["0-4294967295"]),
	"Meta":UcsMoMeta("AaaLdapProvider", "aaaLdapProvider", "provider-[Name]", _VersionMeta.Version101e, "InputOutput", 0x3ffffL, [], [u'aaaLdapGroupRule'], ["Add", "Get", "Remove", "Set"], ["aaa", "admin"])
}

