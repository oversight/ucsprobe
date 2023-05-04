import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtIfFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtIfFsmStage")

	@staticmethod
	def ClassId():
		return "mgmtIfFsmStage"

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
	CONST_NAME_DISABLE_VIP_BEGIN = "DisableVipBegin"
	CONST_NAME_DISABLE_VIP_FAIL = "DisableVipFail"
	CONST_NAME_DISABLE_VIP_PEER = "DisableVipPeer"
	CONST_NAME_DISABLE_VIP_SUCCESS = "DisableVipSuccess"
	CONST_NAME_ENABLE_HABEGIN = "EnableHABegin"
	CONST_NAME_ENABLE_HAFAIL = "EnableHAFail"
	CONST_NAME_ENABLE_HALOCAL = "EnableHALocal"
	CONST_NAME_ENABLE_HASUCCESS = "EnableHASuccess"
	CONST_NAME_ENABLE_VIP_BEGIN = "EnableVipBegin"
	CONST_NAME_ENABLE_VIP_FAIL = "EnableVipFail"
	CONST_NAME_ENABLE_VIP_LOCAL = "EnableVipLocal"
	CONST_NAME_ENABLE_VIP_SUCCESS = "EnableVipSuccess"
	CONST_NAME_SW_MGMT_INBAND_IF_CONFIG_BEGIN = "SwMgmtInbandIfConfigBegin"
	CONST_NAME_SW_MGMT_INBAND_IF_CONFIG_FAIL = "SwMgmtInbandIfConfigFail"
	CONST_NAME_SW_MGMT_INBAND_IF_CONFIG_SUCCESS = "SwMgmtInbandIfConfigSuccess"
	CONST_NAME_SW_MGMT_INBAND_IF_CONFIG_SWITCH = "SwMgmtInbandIfConfigSwitch"
	CONST_NAME_SW_MGMT_OOB_IF_CONFIG_BEGIN = "SwMgmtOobIfConfigBegin"
	CONST_NAME_SW_MGMT_OOB_IF_CONFIG_FAIL = "SwMgmtOobIfConfigFail"
	CONST_NAME_SW_MGMT_OOB_IF_CONFIG_SUCCESS = "SwMgmtOobIfConfigSuccess"
	CONST_NAME_SW_MGMT_OOB_IF_CONFIG_SWITCH = "SwMgmtOobIfConfigSwitch"
	CONST_NAME_VIRTUAL_IF_CONFIG_BEGIN = "VirtualIfConfigBegin"
	CONST_NAME_VIRTUAL_IF_CONFIG_FAIL = "VirtualIfConfigFail"
	CONST_NAME_VIRTUAL_IF_CONFIG_LOCAL = "VirtualIfConfigLocal"
	CONST_NAME_VIRTUAL_IF_CONFIG_REMOTE = "VirtualIfConfigRemote"
	CONST_NAME_VIRTUAL_IF_CONFIG_SUCCESS = "VirtualIfConfigSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
