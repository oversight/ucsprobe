import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Level":UcsPropertyMeta("Level", "level", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], ["0-4294967295"]),
	"RevertTimeout":UcsPropertyMeta("RevertTimeout", "revertTimeout", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["forever"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EventEpCtrl", "eventEpCtrl", "evctrl", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [], ["Get"], ["admin", "fault", "operations"])
}

