import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ObserveObservedFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ObserveObservedFsmStage")

	@staticmethod
	def ClassId():
		return "observeObservedFsmStage"

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
	CONST_NAME_RESOLVE_CONTROLLER_FSM_BEGIN = "ResolveControllerFsmBegin"
	CONST_NAME_RESOLVE_CONTROLLER_FSM_EXECUTE = "ResolveControllerFsmExecute"
	CONST_NAME_RESOLVE_CONTROLLER_FSM_FAIL = "ResolveControllerFsmFail"
	CONST_NAME_RESOLVE_CONTROLLER_FSM_SUCCESS = "ResolveControllerFsmSuccess"
	CONST_NAME_RESOLVE_POLICY_FSM_BEGIN = "ResolvePolicyFsmBegin"
	CONST_NAME_RESOLVE_POLICY_FSM_EXECUTE = "ResolvePolicyFsmExecute"
	CONST_NAME_RESOLVE_POLICY_FSM_FAIL = "ResolvePolicyFsmFail"
	CONST_NAME_RESOLVE_POLICY_FSM_SUCCESS = "ResolvePolicyFsmSuccess"
	CONST_NAME_RESOLVE_RESOURCE_FSM_BEGIN = "ResolveResourceFsmBegin"
	CONST_NAME_RESOLVE_RESOURCE_FSM_EXECUTE = "ResolveResourceFsmExecute"
	CONST_NAME_RESOLVE_RESOURCE_FSM_FAIL = "ResolveResourceFsmFail"
	CONST_NAME_RESOLVE_RESOURCE_FSM_SUCCESS = "ResolveResourceFsmSuccess"
	CONST_NAME_RESOLVE_VMFSM_BEGIN = "ResolveVMFsmBegin"
	CONST_NAME_RESOLVE_VMFSM_EXECUTE = "ResolveVMFsmExecute"
	CONST_NAME_RESOLVE_VMFSM_FAIL = "ResolveVMFsmFail"
	CONST_NAME_RESOLVE_VMFSM_SUCCESS = "ResolveVMFsmSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
