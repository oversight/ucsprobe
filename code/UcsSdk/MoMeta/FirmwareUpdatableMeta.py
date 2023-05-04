import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["trigger", "triggered"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Deployment":UcsPropertyMeta("Deployment", "deployment", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["backup", "unspecified"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["activating", "auto-activating", "auto-updating", "bad-image", "failed", "pending-next-boot", "pending-power-cycle", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating", "upgrading"], ["0-4294967295"]),
	"OperStateQual":UcsPropertyMeta("OperStateQual", "operStateQual", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["boot-conf-missing", "checksum-failure", "crc-failure", "filesystem-error", "mgmt-connect-error", "none", "unknown-error"], ["0-4294967295"]),
	"PrevVersion":UcsPropertyMeta("PrevVersion", "prevVersion", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Version":UcsPropertyMeta("Version", "version", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("FirmwareUpdatable", "firmwareUpdatable", "fw-updatable", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [u'faultInst', u'firmwareInstallable'], ["Get", "Set"], ["admin"])
}

