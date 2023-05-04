import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ActivityName":UcsPropertyMeta("ActivityName", "activityName", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"FalseHits":UcsPropertyMeta("FalseHits", "falseHits", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-4294967295"]),
	"Label":UcsPropertyMeta("Label", "label", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"TotalPasses":UcsPropertyMeta("TotalPasses", "totalPasses", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, [], ["0-4294967295"]),
	"TrueHits":UcsPropertyMeta("TrueHits", "trueHits", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("SwatResultstats", "swatResultstats", "", _VersionMeta.Version101e, "InputOutput", 0x1ffL, [], [], ["Get"], ["admin"])
}

