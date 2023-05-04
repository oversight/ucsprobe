import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LicenseInstanceFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LicenseInstanceFsmStage")

	@staticmethod
	def ClassId():
		return "licenseInstanceFsmStage"

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
	CONST_NAME_UPDATE_FLEXLM_BEGIN = "UpdateFlexlmBegin"
	CONST_NAME_UPDATE_FLEXLM_FAIL = "UpdateFlexlmFail"
	CONST_NAME_UPDATE_FLEXLM_LOCAL = "UpdateFlexlmLocal"
	CONST_NAME_UPDATE_FLEXLM_REMOTE = "UpdateFlexlmRemote"
	CONST_NAME_UPDATE_FLEXLM_SUCCESS = "UpdateFlexlmSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
