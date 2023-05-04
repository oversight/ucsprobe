import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PortPIoFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PortPIoFsmStage")

	@staticmethod
	def ClassId():
		return "portPIoFsmStage"

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
	CONST_NAME_IN_COMPAT_SFP_PRESENCE_BEGIN = "InCompatSfpPresenceBegin"
	CONST_NAME_IN_COMPAT_SFP_PRESENCE_FAIL = "InCompatSfpPresenceFail"
	CONST_NAME_IN_COMPAT_SFP_PRESENCE_SHUTDOWN = "InCompatSfpPresenceShutdown"
	CONST_NAME_IN_COMPAT_SFP_PRESENCE_SUCCESS = "InCompatSfpPresenceSuccess"
	CONST_NAME_IN_COMPAT_SFP_REPLACED_BEGIN = "InCompatSfpReplacedBegin"
	CONST_NAME_IN_COMPAT_SFP_REPLACED_ENABLE_PORT = "InCompatSfpReplacedEnablePort"
	CONST_NAME_IN_COMPAT_SFP_REPLACED_FAIL = "InCompatSfpReplacedFail"
	CONST_NAME_IN_COMPAT_SFP_REPLACED_SUCCESS = "InCompatSfpReplacedSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
