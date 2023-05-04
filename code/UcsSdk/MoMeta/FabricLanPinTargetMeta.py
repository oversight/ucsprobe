import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"EpDn":UcsPropertyMeta("EpDn", "epDn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"FabricId":UcsPropertyMeta("FabricId", "fabricId", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x8L, None, None, None, ["A", "B", "NONE", "dual"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"TargetStatus":UcsPropertyMeta("TargetStatus", "targetStatus", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["invalid", "valid"], ["0-4294967295"]),
	"Meta":UcsMoMeta("FabricLanPinTarget", "fabricLanPinTarget", "target-[FabricId]", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [u'faultInst'], ["Add", "Get", "Remove", "Set"], ["admin", "ext-lan-config", "ext-lan-policy"])
}

