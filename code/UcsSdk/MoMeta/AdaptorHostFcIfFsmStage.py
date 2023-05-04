import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorHostFcIfFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorHostFcIfFsmStage")

	@staticmethod
	def ClassId():
		return "adaptorHostFcIfFsmStage"

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
	CONST_NAME_CIRCUIT_RESET_BEGIN = "CircuitResetBegin"
	CONST_NAME_CIRCUIT_RESET_DISABLE_A = "CircuitResetDisableA"
	CONST_NAME_CIRCUIT_RESET_DISABLE_B = "CircuitResetDisableB"
	CONST_NAME_CIRCUIT_RESET_ENABLE_A = "CircuitResetEnableA"
	CONST_NAME_CIRCUIT_RESET_ENABLE_B = "CircuitResetEnableB"
	CONST_NAME_CIRCUIT_RESET_FAIL = "CircuitResetFail"
	CONST_NAME_CIRCUIT_RESET_SUCCESS = "CircuitResetSuccess"
	CONST_NAME_RESET_FC_PERS_BINDING_BEGIN = "ResetFcPersBindingBegin"
	CONST_NAME_RESET_FC_PERS_BINDING_EXECUTE_LOCAL = "ResetFcPersBindingExecuteLocal"
	CONST_NAME_RESET_FC_PERS_BINDING_EXECUTE_PEER = "ResetFcPersBindingExecutePeer"
	CONST_NAME_RESET_FC_PERS_BINDING_FAIL = "ResetFcPersBindingFail"
	CONST_NAME_RESET_FC_PERS_BINDING_SUCCESS = "ResetFcPersBindingSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
