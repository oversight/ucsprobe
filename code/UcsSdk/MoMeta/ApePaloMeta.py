import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Description":UcsPropertyMeta("Description", "description", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2L, 0, 510, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"FruId":UcsPropertyMeta("FruId", "fruId", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, 0, 510, None, [], ["0-4294967295"]),
	"HwVersion":UcsPropertyMeta("HwVersion", "hwVersion", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, 0, 510, None, [], ["0-4294967295"]),
	"Mac1":UcsPropertyMeta("Mac1", "mac1", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x20L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"Mac2":UcsPropertyMeta("Mac2", "mac2", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x100L, 0, 256, None, [], ["0-4294967295"]),
	"Serial":UcsPropertyMeta("Serial", "serial", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"StartEvent":UcsPropertyMeta("StartEvent", "startEvent", "uint", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x400L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwBackupVersion":UcsPropertyMeta("SwBackupVersion", "swBackupVersion", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x800L, 0, 510, None, [], ["0-4294967295"]),
	"SwStartupVersion":UcsPropertyMeta("SwStartupVersion", "swStartupVersion", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x1000L, 0, 510, None, [], ["0-4294967295"]),
	"SwVersion":UcsPropertyMeta("SwVersion", "swVersion", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x2000L, 0, 510, None, [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4000L, None, None, None, ["Menlo", "Oplin", "Palo", "Unknown"], ["0-4294967295"]),
	"Meta":UcsMoMeta("ApePalo", "apePalo", "Palo-[Mac1]", _VersionMeta.Version101e, "InputOutput", 0x7fffL, [], [u'apeMenloVnic', u'apePaloVnic'], [None], ["read-only"])
}

