import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version131c, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version131c, UcsPropertyMeta.Naming, 0x4L, 1, 510, None, [], ["0-4294967295"]),
	"ProductName":UcsPropertyMeta("ProductName", "productName", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Revision":UcsPropertyMeta("Revision", "revision", "string", _VersionMeta.Version131c, UcsPropertyMeta.Naming, 0x8L, 1, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version131c, UcsPropertyMeta.Naming, 0x40L, 1, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ComputePlatform", "computePlatform", "manufacturer-[Vendor]-model-[Model]-revision-[Revision]", _VersionMeta.Version131c, "InputOutput", 0x7fL, [], [u'biosSettings'], ["Get"], [""])
}

