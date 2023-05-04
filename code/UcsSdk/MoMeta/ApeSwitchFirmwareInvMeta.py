import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"BiosVersion":UcsPropertyMeta("BiosVersion", "biosVersion", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x1L, 0, 510, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version131c, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Fabric":UcsPropertyMeta("Fabric", "fabric", "string", _VersionMeta.Version131c, UcsPropertyMeta.Naming, 0x8L, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"KsStartupVersion":UcsPropertyMeta("KsStartupVersion", "ksStartupVersion", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x10L, 0, 510, None, [], ["0-4294967295"]),
	"KsVersion":UcsPropertyMeta("KsVersion", "ksVersion", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x20L, 0, 510, None, [], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x40L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SysStartupVersion":UcsPropertyMeta("SysStartupVersion", "sysStartupVersion", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x200L, 0, 510, None, [], ["0-4294967295"]),
	"SysVersion":UcsPropertyMeta("SysVersion", "sysVersion", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x400L, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("ApeSwitchFirmwareInv", "apeSwitchFirmwareInv", "SwitchFirmwareInv-[Fabric]", _VersionMeta.Version131c, "InputOutput", 0x7ffL, [], [], [None], ["read-only"])
}

