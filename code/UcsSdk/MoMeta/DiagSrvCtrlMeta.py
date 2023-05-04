import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["cancel", "ready", "trigger"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version111j, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"EndTs":UcsPropertyMeta("EndTs", "endTs", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], ["0-4294967295"]),
	"EndTsM":UcsPropertyMeta("EndTsM", "endTsM", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["never"], ["0-4294967295"]),
	"ErrorDescr":UcsPropertyMeta("ErrorDescr", "errorDescr", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"ImgLoc":UcsPropertyMeta("ImgLoc", "imgLoc", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"ImgName":UcsPropertyMeta("ImgName", "imgName", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"OperQualifier":UcsPropertyMeta("OperQualifier", "operQualifier", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|not-applicable|stage-failed|test-failure|run-cancelled|component-error|stages-completed),){0,6}(defaultValue|not-applicable|stage-failed|test-failure|run-cancelled|component-error|stages-completed){0,1}""", [], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, None, None, None, None, ["cancelled", "complete", "failed", "in-progress", "not-run", "scheduled"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"RunPolicyName":UcsPropertyMeta("RunPolicyName", "runPolicyName", "string", _VersionMeta.Version131c, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
	"StartTs":UcsPropertyMeta("StartTs", "startTs", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], ["0-4294967295"]),
	"StartTsM":UcsPropertyMeta("StartTsM", "startTsM", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["never"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version111j, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["EFI", "full"], ["0-4294967295"]),
	"Meta":UcsMoMeta("DiagSrvCtrl", "diagSrvCtrl", "diag", _VersionMeta.Version111j, "InputOutput", 0x7fL, [], [u'diagRslt', u'diagRunPolicy', u'etherServerIntFIo'], ["Get"], ["admin", "pn-equipment", "pn-maintenance"])
}

