import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"LargeReceive":UcsPropertyMeta("LargeReceive", "largeReceive", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"TcpRxChecksum":UcsPropertyMeta("TcpRxChecksum", "tcpRxChecksum", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"TcpSegment":UcsPropertyMeta("TcpSegment", "tcpSegment", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"TcpTxChecksum":UcsPropertyMeta("TcpTxChecksum", "tcpTxChecksum", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorEthOffloadProfile", "adaptorEthOffloadProfile", "eth-offload", _VersionMeta.Version101e, "InputOutput", 0xffL, [], [], ["Get", "Set"], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"])
}

