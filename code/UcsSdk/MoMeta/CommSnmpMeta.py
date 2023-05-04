import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Community":UcsPropertyMeta("Community", "community", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, """[!#$%\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{0,32}""", [], ["0-4294967295"]),
	"ConfigState":UcsPropertyMeta("ConfigState", "configState", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applied", "ok"], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"IntId":UcsPropertyMeta("IntId", "intId", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, None, None, None, None, ["none"], ["0-4294967295"]),
	"IsSetSnmpSecure":UcsPropertyMeta("IsSetSnmpSecure", "isSetSnmpSecure", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.CreateOnly, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"OperPort":UcsPropertyMeta("OperPort", "operPort", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-65535"]),
	"PolicyLevel":UcsPropertyMeta("PolicyLevel", "policyLevel", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"PolicyOwner":UcsPropertyMeta("PolicyOwner", "policyOwner", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["local", "pending-policy", "policy"], ["0-4294967295"]),
	"Port":UcsPropertyMeta("Port", "port", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-65535"]),
	"Proto":UcsPropertyMeta("Proto", "proto", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["all", "none", "tcp", "udp"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x100L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SysContact":UcsPropertyMeta("SysContact", "sysContact", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x400L, 0, 255, None, [], ["0-4294967295"]),
	"SysLocation":UcsPropertyMeta("SysLocation", "sysLocation", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x800L, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("CommSnmp", "commSnmp", "snmp-svc", _VersionMeta.Version101e, "InputOutput", 0xfffL, [], [u'commSnmpTrap', u'commSnmpUser', u'faultInst'], ["Get", "Set"], ["aaa", "admin"])
}

