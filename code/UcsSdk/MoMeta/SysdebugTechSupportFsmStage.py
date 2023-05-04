import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysdebugTechSupportFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysdebugTechSupportFsmStage")

	@staticmethod
	def ClassId():
		return "sysdebugTechSupportFsmStage"

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
	CONST_NAME_DELETE_TECH_SUP_FILE_BEGIN = "DeleteTechSupFileBegin"
	CONST_NAME_DELETE_TECH_SUP_FILE_FAIL = "DeleteTechSupFileFail"
	CONST_NAME_DELETE_TECH_SUP_FILE_LOCAL = "DeleteTechSupFileLocal"
	CONST_NAME_DELETE_TECH_SUP_FILE_PEER = "DeleteTechSupFilePeer"
	CONST_NAME_DELETE_TECH_SUP_FILE_SUCCESS = "DeleteTechSupFileSuccess"
	CONST_NAME_DOWNLOAD_BEGIN = "DownloadBegin"
	CONST_NAME_DOWNLOAD_COPY_PRIMARY = "DownloadCopyPrimary"
	CONST_NAME_DOWNLOAD_COPY_SUB = "DownloadCopySub"
	CONST_NAME_DOWNLOAD_DELETE_PRIMARY = "DownloadDeletePrimary"
	CONST_NAME_DOWNLOAD_DELETE_SUB = "DownloadDeleteSub"
	CONST_NAME_DOWNLOAD_FAIL = "DownloadFail"
	CONST_NAME_DOWNLOAD_SUCCESS = "DownloadSuccess"
	CONST_NAME_INITIATE_BEGIN = "InitiateBegin"
	CONST_NAME_INITIATE_FAIL = "InitiateFail"
	CONST_NAME_INITIATE_LOCAL = "InitiateLocal"
	CONST_NAME_INITIATE_SUCCESS = "InitiateSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
