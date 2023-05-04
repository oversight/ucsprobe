import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"LldpMacOffset1":UcsPropertyMeta("LldpMacOffset1", "lldpMacOffset1", "byte", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["0-4294967295"]),
	"LldpMacOffset2":UcsPropertyMeta("LldpMacOffset2", "lldpMacOffset2", "byte", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-4294967295"]),
	"MacOffset1":UcsPropertyMeta("MacOffset1", "macOffset1", "byte", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["0-4294967295"]),
	"MacOffset2":UcsPropertyMeta("MacOffset2", "macOffset2", "byte", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, [], ["0-4294967295"]),
	"MacOffsetSub00":UcsPropertyMeta("MacOffsetSub00", "macOffsetSub00", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["0-4294967295"]),
	"MacOffsetSub01":UcsPropertyMeta("MacOffsetSub01", "macOffsetSub01", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, [], ["0-4294967295"]),
	"MacOffsetSub02":UcsPropertyMeta("MacOffsetSub02", "macOffsetSub02", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, [], ["0-4294967295"]),
	"MacOffsetSub03":UcsPropertyMeta("MacOffsetSub03", "macOffsetSub03", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, [], ["0-4294967295"]),
	"MacOffsetSub10":UcsPropertyMeta("MacOffsetSub10", "macOffsetSub10", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x400L, None, None, None, [], ["0-4294967295"]),
	"MacOffsetSub11":UcsPropertyMeta("MacOffsetSub11", "macOffsetSub11", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, [], ["0-4294967295"]),
	"MacOffsetSub12":UcsPropertyMeta("MacOffsetSub12", "macOffsetSub12", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x1000L, None, None, None, [], ["0-4294967295"]),
	"MacOffsetSub13":UcsPropertyMeta("MacOffsetSub13", "macOffsetSub13", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x2000L, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x4000L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x8000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorUplinkHwAddrCap", "adaptorUplinkHwAddrCap", "hwaddr-uplink", _VersionMeta.Version141i, "InputOutput", 0xffffL, [], [], ["Get"], ["read-only"])
}

