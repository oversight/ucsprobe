import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Format":UcsPropertyMeta("Format", "format", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], ["0-4294967295"]),
	"Mask":UcsPropertyMeta("Mask", "mask", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x8L, None, None, None, ["FF:FF:FF:FF:FF:FF:FF:Fx", "FF:FF:FF:FF:FF:FF:FF:xx", "FF:FF:FF:FF:FF:FF:Fx:xx", "FF:FF:FF:FF:FF:FF:xx:xx", "FF:FF:FF:FF:FF:Fx:xx:xx", "FF:FF:FF:FF:FF:xx:xx:xx", "FF:FF:FF:FF:Fx:xx:xx:xx", "FF:FF:FF:FF:xx:xx:xx:xx", "FF:FF:FF:Fx:xx:xx:xx:xx", "FF:FF:FF:xx:xx:xx:xx:xx", "FF:FF:Fx:xx:xx:xx:xx:xx", "FF:FF:xx:xx:xx:xx:xx:xx", "FF:Fx:xx:xx:xx:xx:xx:xx", "FF:xx:xx:xx:xx:xx:xx:xx", "Fx:xx:xx:xx:xx:xx:xx:xx"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("FcpoolFormat", "fcpoolFormat", "format-[Format]-[Mask]", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [], ["Get"], ["admin", "ext-san-config", "ext-san-policy", "ls-storage", "ls-storage-policy"])
}

