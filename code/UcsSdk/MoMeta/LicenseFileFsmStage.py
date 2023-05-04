import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LicenseFileFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LicenseFileFsmStage")

	@staticmethod
	def ClassId():
		return "licenseFileFsmStage"

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
	CONST_NAME_CLEAR_BEGIN = "ClearBegin"
	CONST_NAME_CLEAR_FAIL = "ClearFail"
	CONST_NAME_CLEAR_LOCAL = "ClearLocal"
	CONST_NAME_CLEAR_REMOTE = "ClearRemote"
	CONST_NAME_CLEAR_SUCCESS = "ClearSuccess"
	CONST_NAME_INSTALL_BEGIN = "InstallBegin"
	CONST_NAME_INSTALL_FAIL = "InstallFail"
	CONST_NAME_INSTALL_LOCAL = "InstallLocal"
	CONST_NAME_INSTALL_REMOTE = "InstallRemote"
	CONST_NAME_INSTALL_SUCCESS = "InstallSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
