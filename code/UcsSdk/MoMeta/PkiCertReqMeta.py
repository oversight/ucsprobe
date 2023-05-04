import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Country":UcsPropertyMeta("Country", "country", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x2L, None, None, """^([A-Z]{2})?$""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Dns":UcsPropertyMeta("Dns", "dns", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,255}""", [], ["0-4294967295"]),
	"Email":UcsPropertyMeta("Email", "email", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,40}""", [], ["0-4294967295"]),
	"Ip":UcsPropertyMeta("Ip", "ip", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"IpA":UcsPropertyMeta("IpA", "ipA", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x40L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"IpB":UcsPropertyMeta("IpB", "ipB", "string", _VersionMeta.Version212a, UcsPropertyMeta.ReadWrite, 0x80L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], ["0-4294967295"]),
	"Ipv6":UcsPropertyMeta("Ipv6", "ipv6", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x100L, 0, 256, None, [], ["0-4294967295"]),
	"Ipv6A":UcsPropertyMeta("Ipv6A", "ipv6A", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x200L, 0, 256, None, [], ["0-4294967295"]),
	"Ipv6B":UcsPropertyMeta("Ipv6B", "ipv6B", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x400L, 0, 256, None, [], ["0-4294967295"]),
	"Locality":UcsPropertyMeta("Locality", "locality", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], ["0-4294967295"]),
	"OrgName":UcsPropertyMeta("OrgName", "orgName", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, """[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], ["0-4294967295"]),
	"OrgUnitName":UcsPropertyMeta("OrgUnitName", "orgUnitName", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, """[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], ["0-4294967295"]),
	"Pwd":UcsPropertyMeta("Pwd", "pwd", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4000L, None, None, None, [], ["0-4294967295"]),
	"Req":UcsPropertyMeta("Req", "req", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8000L, 0, 256, None, [], ["0-4294967295"]),
	"State":UcsPropertyMeta("State", "state", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x10000L, None, None, """[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SubjName":UcsPropertyMeta("SubjName", "subjName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40000L, 0, 64, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("PkiCertReq", "pkiCertReq", "certreq", _VersionMeta.Version101e, "InputOutput", 0x7ffffL, [], [], ["Add", "Get", "Remove", "Set"], ["aaa", "admin"])
}

