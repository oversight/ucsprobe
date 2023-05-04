import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PolicyPolicyScopeFsmTask(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PolicyPolicyScopeFsmTask")

	@staticmethod
	def ClassId():
		return "policyPolicyScopeFsmTask"

	COMPLETION = "Completion"
	DN = "Dn"
	FLAGS = "Flags"
	ITEM = "Item"
	RN = "Rn"
	SEQ_ID = "SeqId"
	STATUS = "Status"

	CONST_COMPLETION_CANCELLED = "cancelled"
	CONST_COMPLETION_COMPLETED = "completed"
	CONST_COMPLETION_PROCESSING = "processing"
	CONST_COMPLETION_SCHEDULED = "scheduled"
	CONST_ITEM_RELEASE_ALL_OPERATION_FSM = "ReleaseAllOperationFsm"
	CONST_ITEM_RELEASE_ALL_POLICY_FSM = "ReleaseAllPolicyFsm"
	CONST_ITEM_RELEASE_ALL_STORAGE_FSM = "ReleaseAllStorageFsm"
	CONST_ITEM_RELEASE_MANY_OPERATION_FSM = "ReleaseManyOperationFsm"
	CONST_ITEM_RELEASE_MANY_POLICY_FSM = "ReleaseManyPolicyFsm"
	CONST_ITEM_RELEASE_MANY_STORAGE_FSM = "ReleaseManyStorageFsm"
	CONST_ITEM_RELEASE_OPERATION_FSM = "ReleaseOperationFsm"
	CONST_ITEM_RELEASE_POLICY_FSM = "ReleasePolicyFsm"
	CONST_ITEM_RELEASE_STORAGE_FSM = "ReleaseStorageFsm"
	CONST_ITEM_RESOLVE_ALL_OPERATION_FSM = "ResolveAllOperationFsm"
	CONST_ITEM_RESOLVE_ALL_POLICY_FSM = "ResolveAllPolicyFsm"
	CONST_ITEM_RESOLVE_ALL_STORAGE_FSM = "ResolveAllStorageFsm"
	CONST_ITEM_RESOLVE_MANY_OPERATION_FSM = "ResolveManyOperationFsm"
	CONST_ITEM_RESOLVE_MANY_POLICY_FSM = "ResolveManyPolicyFsm"
	CONST_ITEM_RESOLVE_MANY_STORAGE_FSM = "ResolveManyStorageFsm"
	CONST_ITEM_NOP = "nop"
