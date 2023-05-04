import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"DefQuant":UcsPropertyMeta("DefQuant", "defQuant", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, [], ["0-4294967295"]),
	"Deleted":UcsPropertyMeta("Deleted", "deleted", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Deprecated":UcsPropertyMeta("Deprecated", "deprecated", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"ElementLoadFailures":UcsPropertyMeta("ElementLoadFailures", "elementLoadFailures", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ElementsLoaded":UcsPropertyMeta("ElementsLoaded", "elementsLoaded", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"FeatureName":UcsPropertyMeta("FeatureName", "featureName", "string", _VersionMeta.Version141i, UcsPropertyMeta.Naming, 0x8L, 1, 64, None, [], ["0-4294967295"]),
	"Gencount":UcsPropertyMeta("Gencount", "gencount", "uint", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"GracePeriod":UcsPropertyMeta("GracePeriod", "gracePeriod", "ulong", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["0-4294967295"]),
	"LicVendor":UcsPropertyMeta("LicVendor", "licVendor", "string", _VersionMeta.Version141i, UcsPropertyMeta.Naming, 0x20L, 1, 510, None, [], ["0-4294967295"]),
	"LicVersion":UcsPropertyMeta("LicVersion", "licVersion", "string", _VersionMeta.Version141i, UcsPropertyMeta.Naming, 0x40L, 1, 510, None, [], ["0-4294967295"]),
	"LoadErrors":UcsPropertyMeta("LoadErrors", "loadErrors", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"LoadWarnings":UcsPropertyMeta("LoadWarnings", "loadWarnings", "uint", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"MgmtPlaneVer":UcsPropertyMeta("MgmtPlaneVer", "mgmtPlaneVer", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version141i, UcsPropertyMeta.Naming, 0x80L, 1, 510, None, [], ["0-4294967295"]),
	"Revision":UcsPropertyMeta("Revision", "revision", "string", _VersionMeta.Version141i, UcsPropertyMeta.Naming, 0x100L, 1, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x200L, 0, 256, None, [], ["0-4294967295"]),
	"Sku":UcsPropertyMeta("Sku", "sku", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x800L, None, None, None, ["boolean", "counted"], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version141i, UcsPropertyMeta.Naming, 0x1000L, 1, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("LicenseFeatureCapProvider", "licenseFeatureCapProvider", "feature-[FeatureName]-[LicVendor]|[LicVersion]manufacturer-[Vendor]-model-[Model]-revision-[Revision]", _VersionMeta.Version141i, "InputOutput", 0x1fffL, [], [], ["Get"], [""])
}

