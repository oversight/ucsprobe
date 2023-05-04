import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version222c, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"ExportFailureReason":UcsPropertyMeta("ExportFailureReason", "exportFailureReason", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"ExportStatus":UcsPropertyMeta("ExportStatus", "exportStatus", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, None, None, None, ["failure", "success"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadWrite, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"SwitchId":UcsPropertyMeta("SwitchId", "switchId", "string", _VersionMeta.Version222c, UcsPropertyMeta.Naming, 0x10L, None, None, None, ["A", "B", "NONE"], ["0-4294967295"]),
	"Meta":UcsMoMeta("SysdebugLogExportStatus", "sysdebugLogExportStatus", "log-export-status-[SwitchId]", _VersionMeta.Version222c, "InputOutput", 0x1fL, [], [u'faultInst'], [None], ["read-only"])
}

