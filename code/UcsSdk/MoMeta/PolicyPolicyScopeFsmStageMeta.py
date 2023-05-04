import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"LastUpdateTime":UcsPropertyMeta("LastUpdateTime", "lastUpdateTime", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], ["0-4294967295"]),
	"Name":UcsPropertyMeta("Name", "name", "string", _VersionMeta.Version211a, UcsPropertyMeta.Naming, None, None, None, None, ["ReleaseAllOperationFsmBegin", "ReleaseAllOperationFsmFail", "ReleaseAllOperationFsmReleaseAll", "ReleaseAllOperationFsmSuccess", "ReleaseAllPolicyFsmBegin", "ReleaseAllPolicyFsmFail", "ReleaseAllPolicyFsmReleaseAll", "ReleaseAllPolicyFsmSuccess", "ReleaseAllStorageFsmBegin", "ReleaseAllStorageFsmFail", "ReleaseAllStorageFsmReleaseAll", "ReleaseAllStorageFsmSuccess", "ReleaseManyOperationFsmBegin", "ReleaseManyOperationFsmFail", "ReleaseManyOperationFsmReleaseMany", "ReleaseManyOperationFsmSuccess", "ReleaseManyPolicyFsmBegin", "ReleaseManyPolicyFsmFail", "ReleaseManyPolicyFsmReleaseMany", "ReleaseManyPolicyFsmSuccess", "ReleaseManyStorageFsmBegin", "ReleaseManyStorageFsmFail", "ReleaseManyStorageFsmReleaseMany", "ReleaseManyStorageFsmSuccess", "ReleaseOperationFsmBegin", "ReleaseOperationFsmFail", "ReleaseOperationFsmRelease", "ReleaseOperationFsmSuccess", "ReleasePolicyFsmBegin", "ReleasePolicyFsmFail", "ReleasePolicyFsmRelease", "ReleasePolicyFsmSuccess", "ReleaseStorageFsmBegin", "ReleaseStorageFsmFail", "ReleaseStorageFsmRelease", "ReleaseStorageFsmSuccess", "ResolveAllOperationFsmBegin", "ResolveAllOperationFsmFail", "ResolveAllOperationFsmResolveAll", "ResolveAllOperationFsmSuccess", "ResolveAllPolicyFsmBegin", "ResolveAllPolicyFsmFail", "ResolveAllPolicyFsmResolveAll", "ResolveAllPolicyFsmSuccess", "ResolveAllStorageFsmBegin", "ResolveAllStorageFsmFail", "ResolveAllStorageFsmResolveAll", "ResolveAllStorageFsmSuccess", "ResolveManyOperationFsmBegin", "ResolveManyOperationFsmFail", "ResolveManyOperationFsmResolveMany", "ResolveManyOperationFsmSuccess", "ResolveManyPolicyFsmBegin", "ResolveManyPolicyFsmFail", "ResolveManyPolicyFsmResolveMany", "ResolveManyPolicyFsmSuccess", "ResolveManyStorageFsmBegin", "ResolveManyStorageFsmFail", "ResolveManyStorageFsmResolveMany", "ResolveManyStorageFsmSuccess", "nop"], ["0-4294967295"]),
	"Order":UcsPropertyMeta("Order", "order", "ushort", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Retry":UcsPropertyMeta("Retry", "retry", "byte", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"StageStatus":UcsPropertyMeta("StageStatus", "stageStatus", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, None, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Meta":UcsMoMeta("PolicyPolicyScopeFsmStage", "policyPolicyScopeFsmStage", "stage-[Name]", _VersionMeta.Version211a, "OutputOnly", 0x0L, [], [], [None], [""])
}

