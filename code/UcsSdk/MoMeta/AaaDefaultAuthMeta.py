import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"OperProviderGroup":UcsPropertyMeta("OperProviderGroup", "operProviderGroup", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 127, None, [], ["0-4294967295"]),
	"OperRealm":UcsPropertyMeta("OperRealm", "operRealm", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["ldap", "local", "none", "radius", "tacacs"], ["0-4294967295"]),
	"ProviderGroup":UcsPropertyMeta("ProviderGroup", "providerGroup", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x10L, 0, 127, None, [], ["0-4294967295"]),
	"Realm":UcsPropertyMeta("Realm", "realm", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["ldap", "local", "none", "radius", "tacacs"], ["0-4294967295"]),
	"RefreshPeriod":UcsPropertyMeta("RefreshPeriod", "refreshPeriod", "uint", _VersionMeta.Version203a, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["60-172800"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"SessionTimeout":UcsPropertyMeta("SessionTimeout", "sessionTimeout", "uint", _VersionMeta.Version203a, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, [], ["60-172800"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Use2Factor":UcsPropertyMeta("Use2Factor", "use2Factor", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Meta":UcsMoMeta("AaaDefaultAuth", "aaaDefaultAuth", "default-auth", _VersionMeta.Version141i, "InputOutput", 0x7ffL, [], [u'faultInst'], ["Get", "Set"], ["aaa", "admin"])
}

