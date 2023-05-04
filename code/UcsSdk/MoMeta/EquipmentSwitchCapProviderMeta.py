import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Deleted":UcsPropertyMeta("Deleted", "deleted", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Deprecated":UcsPropertyMeta("Deprecated", "deprecated", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"ElementLoadFailures":UcsPropertyMeta("ElementLoadFailures", "elementLoadFailures", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ElementsLoaded":UcsPropertyMeta("ElementsLoaded", "elementsLoaded", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Gencount":UcsPropertyMeta("Gencount", "gencount", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LoadErrors":UcsPropertyMeta("LoadErrors", "loadErrors", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LoadWarnings":UcsPropertyMeta("LoadWarnings", "loadWarnings", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MgmtPlaneVer":UcsPropertyMeta("MgmtPlaneVer", "mgmtPlaneVer", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, 1, 510, None, [], ["0-4294967295"]),
	"PromCardType":UcsPropertyMeta("PromCardType", "promCardType", "ushort", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-4294967295"]),
	"Revision":UcsPropertyMeta("Revision", "revision", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x10L, 1, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x80L, 1, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("EquipmentSwitchCapProvider", "equipmentSwitchCapProvider", "manufacturer-[Vendor]-model-[Model]-revision-[Revision]", _VersionMeta.Version101e, "InputOutput", 0xffL, [], [u'equipmentBeaconCapProvider', u'equipmentManufacturingDef', u'equipmentPhysicalDef', u'equipmentPicture', u'equipmentPortGroupAggregationDef', u'equipmentPortGroupSwComplexDef', u'equipmentServiceDef', u'equipmentSlotArray', u'equipmentSlotArrayRef', u'equipmentSwitchCap', u'equipmentUnifiedPortCapProvider', u'firmwareType', u'firmwareUpgradeConstraint'], ["Get"], [""])
}

