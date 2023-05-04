import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LicenseDownloaderFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LicenseDownloaderFsmStage")

	@staticmethod
	def ClassId():
		return "licenseDownloaderFsmStage"

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
	CONST_NAME_DOWNLOAD_BEGIN = "DownloadBegin"
	CONST_NAME_DOWNLOAD_COPY_REMOTE = "DownloadCopyRemote"
	CONST_NAME_DOWNLOAD_DELETE_LOCAL = "DownloadDeleteLocal"
	CONST_NAME_DOWNLOAD_DELETE_REMOTE = "DownloadDeleteRemote"
	CONST_NAME_DOWNLOAD_FAIL = "DownloadFail"
	CONST_NAME_DOWNLOAD_LOCAL = "DownloadLocal"
	CONST_NAME_DOWNLOAD_SUCCESS = "DownloadSuccess"
	CONST_NAME_DOWNLOAD_VALIDATE_LOCAL = "DownloadValidateLocal"
	CONST_NAME_DOWNLOAD_VALIDATE_REMOTE = "DownloadValidateRemote"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
