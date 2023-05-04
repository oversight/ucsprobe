import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PolicyPolicyScopeFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PolicyPolicyScopeFsmStage")

	@staticmethod
	def ClassId():
		return "policyPolicyScopeFsmStage"

	DESCR = "Descr"
	DN = "Dn"
	LAST_UPDATE_TIME = "LastUpdateTime"
	NAME = "Name"
	ORDER = "Order"
	RETRY = "Retry"
	RN = "Rn"
	STAGE_STATUS = "StageStatus"
	STATUS = "Status"

	CONST_LAST_UPDATE_TIME_ = ""
	CONST_NAME_RELEASE_ALL_OPERATION_FSM_BEGIN = "ReleaseAllOperationFsmBegin"
	CONST_NAME_RELEASE_ALL_OPERATION_FSM_FAIL = "ReleaseAllOperationFsmFail"
	CONST_NAME_RELEASE_ALL_OPERATION_FSM_RELEASE_ALL = "ReleaseAllOperationFsmReleaseAll"
	CONST_NAME_RELEASE_ALL_OPERATION_FSM_SUCCESS = "ReleaseAllOperationFsmSuccess"
	CONST_NAME_RELEASE_ALL_POLICY_FSM_BEGIN = "ReleaseAllPolicyFsmBegin"
	CONST_NAME_RELEASE_ALL_POLICY_FSM_FAIL = "ReleaseAllPolicyFsmFail"
	CONST_NAME_RELEASE_ALL_POLICY_FSM_RELEASE_ALL = "ReleaseAllPolicyFsmReleaseAll"
	CONST_NAME_RELEASE_ALL_POLICY_FSM_SUCCESS = "ReleaseAllPolicyFsmSuccess"
	CONST_NAME_RELEASE_ALL_STORAGE_FSM_BEGIN = "ReleaseAllStorageFsmBegin"
	CONST_NAME_RELEASE_ALL_STORAGE_FSM_FAIL = "ReleaseAllStorageFsmFail"
	CONST_NAME_RELEASE_ALL_STORAGE_FSM_RELEASE_ALL = "ReleaseAllStorageFsmReleaseAll"
	CONST_NAME_RELEASE_ALL_STORAGE_FSM_SUCCESS = "ReleaseAllStorageFsmSuccess"
	CONST_NAME_RELEASE_MANY_OPERATION_FSM_BEGIN = "ReleaseManyOperationFsmBegin"
	CONST_NAME_RELEASE_MANY_OPERATION_FSM_FAIL = "ReleaseManyOperationFsmFail"
	CONST_NAME_RELEASE_MANY_OPERATION_FSM_RELEASE_MANY = "ReleaseManyOperationFsmReleaseMany"
	CONST_NAME_RELEASE_MANY_OPERATION_FSM_SUCCESS = "ReleaseManyOperationFsmSuccess"
	CONST_NAME_RELEASE_MANY_POLICY_FSM_BEGIN = "ReleaseManyPolicyFsmBegin"
	CONST_NAME_RELEASE_MANY_POLICY_FSM_FAIL = "ReleaseManyPolicyFsmFail"
	CONST_NAME_RELEASE_MANY_POLICY_FSM_RELEASE_MANY = "ReleaseManyPolicyFsmReleaseMany"
	CONST_NAME_RELEASE_MANY_POLICY_FSM_SUCCESS = "ReleaseManyPolicyFsmSuccess"
	CONST_NAME_RELEASE_MANY_STORAGE_FSM_BEGIN = "ReleaseManyStorageFsmBegin"
	CONST_NAME_RELEASE_MANY_STORAGE_FSM_FAIL = "ReleaseManyStorageFsmFail"
	CONST_NAME_RELEASE_MANY_STORAGE_FSM_RELEASE_MANY = "ReleaseManyStorageFsmReleaseMany"
	CONST_NAME_RELEASE_MANY_STORAGE_FSM_SUCCESS = "ReleaseManyStorageFsmSuccess"
	CONST_NAME_RELEASE_OPERATION_FSM_BEGIN = "ReleaseOperationFsmBegin"
	CONST_NAME_RELEASE_OPERATION_FSM_FAIL = "ReleaseOperationFsmFail"
	CONST_NAME_RELEASE_OPERATION_FSM_RELEASE = "ReleaseOperationFsmRelease"
	CONST_NAME_RELEASE_OPERATION_FSM_SUCCESS = "ReleaseOperationFsmSuccess"
	CONST_NAME_RELEASE_POLICY_FSM_BEGIN = "ReleasePolicyFsmBegin"
	CONST_NAME_RELEASE_POLICY_FSM_FAIL = "ReleasePolicyFsmFail"
	CONST_NAME_RELEASE_POLICY_FSM_RELEASE = "ReleasePolicyFsmRelease"
	CONST_NAME_RELEASE_POLICY_FSM_SUCCESS = "ReleasePolicyFsmSuccess"
	CONST_NAME_RELEASE_STORAGE_FSM_BEGIN = "ReleaseStorageFsmBegin"
	CONST_NAME_RELEASE_STORAGE_FSM_FAIL = "ReleaseStorageFsmFail"
	CONST_NAME_RELEASE_STORAGE_FSM_RELEASE = "ReleaseStorageFsmRelease"
	CONST_NAME_RELEASE_STORAGE_FSM_SUCCESS = "ReleaseStorageFsmSuccess"
	CONST_NAME_RESOLVE_ALL_OPERATION_FSM_BEGIN = "ResolveAllOperationFsmBegin"
	CONST_NAME_RESOLVE_ALL_OPERATION_FSM_FAIL = "ResolveAllOperationFsmFail"
	CONST_NAME_RESOLVE_ALL_OPERATION_FSM_RESOLVE_ALL = "ResolveAllOperationFsmResolveAll"
	CONST_NAME_RESOLVE_ALL_OPERATION_FSM_SUCCESS = "ResolveAllOperationFsmSuccess"
	CONST_NAME_RESOLVE_ALL_POLICY_FSM_BEGIN = "ResolveAllPolicyFsmBegin"
	CONST_NAME_RESOLVE_ALL_POLICY_FSM_FAIL = "ResolveAllPolicyFsmFail"
	CONST_NAME_RESOLVE_ALL_POLICY_FSM_RESOLVE_ALL = "ResolveAllPolicyFsmResolveAll"
	CONST_NAME_RESOLVE_ALL_POLICY_FSM_SUCCESS = "ResolveAllPolicyFsmSuccess"
	CONST_NAME_RESOLVE_ALL_STORAGE_FSM_BEGIN = "ResolveAllStorageFsmBegin"
	CONST_NAME_RESOLVE_ALL_STORAGE_FSM_FAIL = "ResolveAllStorageFsmFail"
	CONST_NAME_RESOLVE_ALL_STORAGE_FSM_RESOLVE_ALL = "ResolveAllStorageFsmResolveAll"
	CONST_NAME_RESOLVE_ALL_STORAGE_FSM_SUCCESS = "ResolveAllStorageFsmSuccess"
	CONST_NAME_RESOLVE_MANY_OPERATION_FSM_BEGIN = "ResolveManyOperationFsmBegin"
	CONST_NAME_RESOLVE_MANY_OPERATION_FSM_FAIL = "ResolveManyOperationFsmFail"
	CONST_NAME_RESOLVE_MANY_OPERATION_FSM_RESOLVE_MANY = "ResolveManyOperationFsmResolveMany"
	CONST_NAME_RESOLVE_MANY_OPERATION_FSM_SUCCESS = "ResolveManyOperationFsmSuccess"
	CONST_NAME_RESOLVE_MANY_POLICY_FSM_BEGIN = "ResolveManyPolicyFsmBegin"
	CONST_NAME_RESOLVE_MANY_POLICY_FSM_FAIL = "ResolveManyPolicyFsmFail"
	CONST_NAME_RESOLVE_MANY_POLICY_FSM_RESOLVE_MANY = "ResolveManyPolicyFsmResolveMany"
	CONST_NAME_RESOLVE_MANY_POLICY_FSM_SUCCESS = "ResolveManyPolicyFsmSuccess"
	CONST_NAME_RESOLVE_MANY_STORAGE_FSM_BEGIN = "ResolveManyStorageFsmBegin"
	CONST_NAME_RESOLVE_MANY_STORAGE_FSM_FAIL = "ResolveManyStorageFsmFail"
	CONST_NAME_RESOLVE_MANY_STORAGE_FSM_RESOLVE_MANY = "ResolveManyStorageFsmResolveMany"
	CONST_NAME_RESOLVE_MANY_STORAGE_FSM_SUCCESS = "ResolveManyStorageFsmSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
