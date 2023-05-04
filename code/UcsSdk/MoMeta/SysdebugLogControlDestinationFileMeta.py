import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"BackupCount":UcsPropertyMeta("BackupCount", "backupCount", "ushort", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, [], ["1-9"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"DefaultLevel":UcsPropertyMeta("DefaultLevel", "defaultLevel", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["crit", "debug0", "debug1", "debug2", "debug3", "debug4", "info", "major", "minor", "warn"], ["0-4294967295"]),
	"DefaultSize":UcsPropertyMeta("DefaultSize", "defaultSize", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["1000000-20000000"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Level":UcsPropertyMeta("Level", "level", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["crit", "debug0", "debug1", "debug2", "debug3", "debug4", "info", "major", "minor", "warn"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x40L, 0, 256, None, [], ["0-4294967295"]),
	"Size":UcsPropertyMeta("Size", "size", "uint", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, [], ["1000000-20000000"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("SysdebugLogControlDestinationFile", "sysdebugLogControlDestinationFile", "file", _VersionMeta.Version101e, "InputOutput", 0x1ffL, [], [], ["Get"], ["admin", "operations"])
}

