import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"CurrentZonePrefix":UcsPropertyMeta("CurrentZonePrefix", "currentZonePrefix", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Lc":UcsPropertyMeta("Lc", "lc", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """[\-\.:_a-zA-Z0-9]{1,64}""", [], ["0-4294967295"]),
	"OldZonePrefix":UcsPropertyMeta("OldZonePrefix", "oldZonePrefix", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("SwFcZoneSet", "swFcZoneSet", "zone-set-default", _VersionMeta.Version211a, "InputOutput", 0xfL, [], [u'swFcServerZoneGroup'], [None], ["read-only"])
}

