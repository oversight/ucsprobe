import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version131c, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Length":UcsPropertyMeta("Length", "length", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["1-1440"]),
	"Order":UcsPropertyMeta("Order", "order", "byte", _VersionMeta.Version131c, UcsPropertyMeta.Naming, 0x8L, None, None, None, [], ["1-64"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["disk", "memory", "memtest", "pci", "processor", "stress"], ["0-4294967295"]),
	"Meta":UcsMoMeta("DiagBladeTest", "diagBladeTest", "blade-test-[Order]", _VersionMeta.Version131c, "InputOutput", 0x7fL, [], [], ["Get"], ["admin", "pn-policy"])
}

