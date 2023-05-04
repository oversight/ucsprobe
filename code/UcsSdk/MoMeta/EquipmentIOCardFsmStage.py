import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentIOCardFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentIOCardFsmStage")

	@staticmethod
	def ClassId():
		return "equipmentIOCardFsmStage"

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
	CONST_NAME_FE_CONN_BEGIN = "FeConnBegin"
	CONST_NAME_FE_CONN_CONFIGURE_END_POINT = "FeConnConfigureEndPoint"
	CONST_NAME_FE_CONN_CONFIGURE_SW_MGMT_END_POINT = "FeConnConfigureSwMgmtEndPoint"
	CONST_NAME_FE_CONN_CONFIGURE_VIF_NS = "FeConnConfigureVifNs"
	CONST_NAME_FE_CONN_DISCOVER_CHASSIS = "FeConnDiscoverChassis"
	CONST_NAME_FE_CONN_ENABLE_CHASSIS = "FeConnEnableChassis"
	CONST_NAME_FE_CONN_FAIL = "FeConnFail"
	CONST_NAME_FE_CONN_SUCCESS = "FeConnSuccess"
	CONST_NAME_FE_PRESENCE_BEGIN = "FePresenceBegin"
	CONST_NAME_FE_PRESENCE_CHECK_LICENSE = "FePresenceCheckLicense"
	CONST_NAME_FE_PRESENCE_FAIL = "FePresenceFail"
	CONST_NAME_FE_PRESENCE_IDENTIFY = "FePresenceIdentify"
	CONST_NAME_FE_PRESENCE_SUCCESS = "FePresenceSuccess"
	CONST_NAME_RESET_CMC_BEGIN = "ResetCmcBegin"
	CONST_NAME_RESET_CMC_EXECUTE = "ResetCmcExecute"
	CONST_NAME_RESET_CMC_FAIL = "ResetCmcFail"
	CONST_NAME_RESET_CMC_SUCCESS = "ResetCmcSuccess"
	CONST_NAME_RESET_IOM_BEGIN = "ResetIomBegin"
	CONST_NAME_RESET_IOM_EXECUTE = "ResetIomExecute"
	CONST_NAME_RESET_IOM_FAIL = "ResetIomFail"
	CONST_NAME_RESET_IOM_SUCCESS = "ResetIomSuccess"
	CONST_NAME_MUX_OFFLINE_BEGIN = "muxOfflineBegin"
	CONST_NAME_MUX_OFFLINE_CLEANUP_ENTRIES = "muxOfflineCleanupEntries"
	CONST_NAME_MUX_OFFLINE_FAIL = "muxOfflineFail"
	CONST_NAME_MUX_OFFLINE_SUCCESS = "muxOfflineSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
