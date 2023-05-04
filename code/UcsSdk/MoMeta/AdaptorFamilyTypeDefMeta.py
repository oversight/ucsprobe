import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version202m, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"IsPassthrough":UcsPropertyMeta("IsPassthrough", "isPassthrough", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"NumDcePorts":UcsPropertyMeta("NumDcePorts", "numDcePorts", "uint", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-4294967295"]),
	"PortFamily":UcsPropertyMeta("PortFamily", "portFamily", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x10L, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x80L, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorFamilyTypeDef", "adaptorFamilyTypeDef", "family-type", _VersionMeta.Version202m, "InputOutput", 0xffL, [], [], ["Get"], ["read-only"])
}

