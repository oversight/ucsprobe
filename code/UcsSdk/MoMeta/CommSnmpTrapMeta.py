import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Community":UcsPropertyMeta("Community", "community", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """[!#$%\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{0,32}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Hostname":UcsPropertyMeta("Hostname", "hostname", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x8L, None, None, """^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], ["0-4294967295"]),
	"NotificationType":UcsPropertyMeta("NotificationType", "notificationType", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["informs", "traps"], ["0-4294967295"]),
	"Port":UcsPropertyMeta("Port", "port", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["1-65535"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"V3Privilege":UcsPropertyMeta("V3Privilege", "v3Privilege", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["auth", "noauth", "priv"], ["0-4294967295"]),
	"Version":UcsPropertyMeta("Version", "version", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["v1", "v2c", "v3"], ["0-4294967295"]),
	"Meta":UcsMoMeta("CommSnmpTrap", "commSnmpTrap", "snmp-trap[Hostname]", _VersionMeta.Version101e, "InputOutput", 0x3ffL, [], [], ["Add", "Get", "Remove", "Set"], ["aaa", "admin"])
}

