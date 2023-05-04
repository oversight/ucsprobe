import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"MacOffset1":UcsPropertyMeta("MacOffset1", "macOffset1", "byte", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["0-4294967295"]),
	"MacOffset2":UcsPropertyMeta("MacOffset2", "macOffset2", "byte", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"WwnReverseMaskA":UcsPropertyMeta("WwnReverseMaskA", "wwnReverseMaskA", "ulong", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["0-4294967295"]),
	"WwnReverseMaskB":UcsPropertyMeta("WwnReverseMaskB", "wwnReverseMaskB", "ulong", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, [], ["0-4294967295"]),
	"WwnnReverseMaskA":UcsPropertyMeta("WwnnReverseMaskA", "wwnnReverseMaskA", "ulong", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, [], ["0-4294967295"]),
	"WwnnReverseMaskB":UcsPropertyMeta("WwnnReverseMaskB", "wwnnReverseMaskB", "ulong", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorHostfcHwAddrCap", "adaptorHostfcHwAddrCap", "hwaddr-hostfc", _VersionMeta.Version141i, "InputOutput", 0x3ffL, [], [], ["Get"], ["read-only"])
}

