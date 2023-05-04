import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"Bytes_eg":UcsPropertyMeta("Bytes_eg", "bytes_eg", "ulong", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, [], ["0-4294967295"]),
	"Bytes_in":UcsPropertyMeta("Bytes_in", "bytes_in", "ulong", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x4L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Dropped_pkts_eg":UcsPropertyMeta("Dropped_pkts_eg", "dropped_pkts_eg", "ulong", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["0-4294967295"]),
	"Dropped_pkts_in":UcsPropertyMeta("Dropped_pkts_in", "dropped_pkts_in", "ulong", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["0-4294967295"]),
	"Errors_eg":UcsPropertyMeta("Errors_eg", "errors_eg", "ulong", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["0-4294967295"]),
	"Errors_in":UcsPropertyMeta("Errors_in", "errors_in", "ulong", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, [], ["0-4294967295"]),
	"Pkts_eg":UcsPropertyMeta("Pkts_eg", "pkts_eg", "ulong", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, [], ["0-4294967295"]),
	"Pkts_in":UcsPropertyMeta("Pkts_in", "pkts_in", "ulong", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x400L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ApePaloVnicStats", "apePaloVnicStats", "palostats", _VersionMeta.Version211a, "InputOutput", 0xfffL, [], [], [None], ["read-only"])
}

