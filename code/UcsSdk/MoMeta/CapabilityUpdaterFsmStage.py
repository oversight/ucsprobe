import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CapabilityUpdaterFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CapabilityUpdaterFsmStage")

	@staticmethod
	def ClassId():
		return "capabilityUpdaterFsmStage"

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
	CONST_NAME_UPDATER_APPLY = "UpdaterApply"
	CONST_NAME_UPDATER_BEGIN = "UpdaterBegin"
	CONST_NAME_UPDATER_COPY_REMOTE = "UpdaterCopyRemote"
	CONST_NAME_UPDATER_DELETE_LOCAL = "UpdaterDeleteLocal"
	CONST_NAME_UPDATER_EVALUATE_STATUS = "UpdaterEvaluateStatus"
	CONST_NAME_UPDATER_FAIL = "UpdaterFail"
	CONST_NAME_UPDATER_LOCAL = "UpdaterLocal"
	CONST_NAME_UPDATER_RESCAN_IMAGES = "UpdaterRescanImages"
	CONST_NAME_UPDATER_SUCCESS = "UpdaterSuccess"
	CONST_NAME_UPDATER_UNPACK_LOCAL = "UpdaterUnpackLocal"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
