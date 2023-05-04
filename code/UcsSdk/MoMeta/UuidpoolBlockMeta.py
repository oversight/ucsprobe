import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"From":UcsPropertyMeta("From", "from", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, None, None, """(([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"To":UcsPropertyMeta("To", "to", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x20L, None, None, """(([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("UuidpoolBlock", "uuidpoolBlock", "block-from-[From]-to-[To]", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [], ["Add", "Get", "Remove"], ["admin", "pn-policy"])
}

