import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"BootToTarget":UcsPropertyMeta("BootToTarget", "bootToTarget", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConnectionTimeOut":UcsPropertyMeta("ConnectionTimeOut", "connectionTimeOut", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["0-255"]),
	"DhcpTimeOut":UcsPropertyMeta("DhcpTimeOut", "dhcpTimeOut", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["60-300"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"HbaMode":UcsPropertyMeta("HbaMode", "hbaMode", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"LunBusyRetryCount":UcsPropertyMeta("LunBusyRetryCount", "lunBusyRetryCount", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["0-60"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"TcpTimeStamp":UcsPropertyMeta("TcpTimeStamp", "tcpTimeStamp", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorProtocolProfile", "adaptorProtocolProfile", "iscsi-prot-profile", _VersionMeta.Version201m, "InputOutput", 0x3ffL, [], [], ["Add", "Get", "Set"], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"])
}

