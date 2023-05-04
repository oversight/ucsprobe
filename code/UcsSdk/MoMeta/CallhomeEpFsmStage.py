import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CallhomeEpFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CallhomeEpFsmStage")

	@staticmethod
	def ClassId():
		return "callhomeEpFsmStage"

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
	CONST_NAME_CONFIG_CALLHOME_BEGIN = "configCallhomeBegin"
	CONST_NAME_CONFIG_CALLHOME_FAIL = "configCallhomeFail"
	CONST_NAME_CONFIG_CALLHOME_SET_LOCAL = "configCallhomeSetLocal"
	CONST_NAME_CONFIG_CALLHOME_SET_PEER = "configCallhomeSetPeer"
	CONST_NAME_CONFIG_CALLHOME_SUCCESS = "configCallhomeSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
