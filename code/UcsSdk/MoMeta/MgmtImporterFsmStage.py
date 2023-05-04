import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtImporterFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtImporterFsmStage")

	@staticmethod
	def ClassId():
		return "mgmtImporterFsmStage"

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
	CONST_NAME_IMPORT_BEGIN = "importBegin"
	CONST_NAME_IMPORT_CONFIG = "importConfig"
	CONST_NAME_IMPORT_DOWNLOAD_LOCAL = "importDownloadLocal"
	CONST_NAME_IMPORT_FAIL = "importFail"
	CONST_NAME_IMPORT_REPORT_RESULTS = "importReportResults"
	CONST_NAME_IMPORT_SUCCESS = "importSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
