import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysfileMutationFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysfileMutationFsmStage")

	@staticmethod
	def ClassId():
		return "sysfileMutationFsmStage"

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
	CONST_NAME_GLOBAL_BEGIN = "GlobalBegin"
	CONST_NAME_GLOBAL_FAIL = "GlobalFail"
	CONST_NAME_GLOBAL_LOCAL = "GlobalLocal"
	CONST_NAME_GLOBAL_PEER = "GlobalPeer"
	CONST_NAME_GLOBAL_SUCCESS = "GlobalSuccess"
	CONST_NAME_SINGLE_BEGIN = "SingleBegin"
	CONST_NAME_SINGLE_EXECUTE = "SingleExecute"
	CONST_NAME_SINGLE_FAIL = "SingleFail"
	CONST_NAME_SINGLE_SUCCESS = "SingleSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
