import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConnectionTimeOut":UcsPropertyMeta("ConnectionTimeOut", "connectionTimeOut", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-255"]),
	"DhcpTimeOut":UcsPropertyMeta("DhcpTimeOut", "dhcpTimeOut", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["60-300"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"FltAggr":UcsPropertyMeta("FltAggr", "fltAggr", "ulong", _VersionMeta.Version201m, UcsPropertyMeta.Internal, None, None, None, None, [], ["0-4294967295"]),
	"InitiatorName":UcsPropertyMeta("InitiatorName", "initiatorName", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"LunBusyRetryCount":UcsPropertyMeta("LunBusyRetryCount", "lunBusyRetryCount", "ushort", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-60"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"TcpTimeStamp":UcsPropertyMeta("TcpTimeStamp", "tcpTimeStamp", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorIscsiProt", "adaptorIscsiProt", "iscsi-prot", _VersionMeta.Version201m, "InputOutput", 0xfL, [], [], [None], ["read-only"])
}

