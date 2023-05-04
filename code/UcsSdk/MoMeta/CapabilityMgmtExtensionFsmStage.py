import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CapabilityMgmtExtensionFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CapabilityMgmtExtensionFsmStage")

	@staticmethod
	def ClassId():
		return "capabilityMgmtExtensionFsmStage"

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
	CONST_NAME_ACTIVATE_MGMT_EXT_APPLY_CATALOG = "ActivateMgmtExtApplyCatalog"
	CONST_NAME_ACTIVATE_MGMT_EXT_BEGIN = "ActivateMgmtExtBegin"
	CONST_NAME_ACTIVATE_MGMT_EXT_COPY_REMOTE = "ActivateMgmtExtCopyRemote"
	CONST_NAME_ACTIVATE_MGMT_EXT_EVALUATE_STATUS = "ActivateMgmtExtEvaluateStatus"
	CONST_NAME_ACTIVATE_MGMT_EXT_FAIL = "ActivateMgmtExtFail"
	CONST_NAME_ACTIVATE_MGMT_EXT_RESCAN_IMAGES = "ActivateMgmtExtRescanImages"
	CONST_NAME_ACTIVATE_MGMT_EXT_SUCCESS = "ActivateMgmtExtSuccess"
	CONST_NAME_ACTIVATE_MGMT_EXT_UNPACK_LOCAL = "ActivateMgmtExtUnpackLocal"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
