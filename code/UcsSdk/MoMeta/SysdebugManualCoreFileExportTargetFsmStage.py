import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysdebugManualCoreFileExportTargetFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysdebugManualCoreFileExportTargetFsmStage")

	@staticmethod
	def ClassId():
		return "sysdebugManualCoreFileExportTargetFsmStage"

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
	CONST_NAME_EXPORT_BEGIN = "ExportBegin"
	CONST_NAME_EXPORT_EXECUTE = "ExportExecute"
	CONST_NAME_EXPORT_FAIL = "ExportFail"
	CONST_NAME_EXPORT_SUCCESS = "ExportSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
