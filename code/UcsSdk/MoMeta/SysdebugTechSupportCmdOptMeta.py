import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChassisCimcId":UcsPropertyMeta("ChassisCimcId", "chassisCimcId", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["all"], ["0-8"]),
	"ChassisId":UcsPropertyMeta("ChassisId", "chassisId", "ushort", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x2L, None, None, None, [], ["1-255"]),
	"ChassisIomId":UcsPropertyMeta("ChassisIomId", "chassisIomId", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, ["all"], ["0-2"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version141i, UcsPropertyMeta.Internal, 0x8L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"CimcAdapterId":UcsPropertyMeta("CimcAdapterId", "cimcAdapterId", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, ["all"], ["0-8"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x20L, 0, 256, None, [], ["0-4294967295"]),
	"FabExtId":UcsPropertyMeta("FabExtId", "fabExtId", "ushort", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, [], ["1-255"]),
	"MajorOptType":UcsPropertyMeta("MajorOptType", "majorOptType", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x80L, None, None, None, ["chassis", "fex", "server", "ucsm", "ucsm-mgmt"], ["0-4294967295"]),
	"RackServerAdapterId":UcsPropertyMeta("RackServerAdapterId", "rackServerAdapterId", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x100L, None, None, None, ["all"], ["0-8"]),
	"RackServerId":UcsPropertyMeta("RackServerId", "rackServerId", "ushort", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, [], ["1-255"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, 0x400L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x800L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("SysdebugTechSupportCmdOpt", "sysdebugTechSupportCmdOpt", "tech-support-cmd-opt", _VersionMeta.Version141i, "InputOutput", 0xfffL, [], [], ["Add", "Get", "Set"], ["admin", "operations"])
}

