import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtBackupFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtBackupFsmStage")

	@staticmethod
	def ClassId():
		return "mgmtBackupFsmStage"

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
	CONST_NAME_BACKUP_BACKUP_LOCAL = "backupBackupLocal"
	CONST_NAME_BACKUP_BEGIN = "backupBegin"
	CONST_NAME_BACKUP_FAIL = "backupFail"
	CONST_NAME_BACKUP_SUCCESS = "backupSuccess"
	CONST_NAME_BACKUP_UPLOAD = "backupUpload"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
