import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtIPv6IfAddrFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtIPv6IfAddrFsmStage")

	@staticmethod
	def ClassId():
		return "mgmtIPv6IfAddrFsmStage"

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
	CONST_NAME_SW_MGMT_OOB_IPV6_IF_CONFIG_BEGIN = "SwMgmtOobIpv6IfConfigBegin"
	CONST_NAME_SW_MGMT_OOB_IPV6_IF_CONFIG_FAIL = "SwMgmtOobIpv6IfConfigFail"
	CONST_NAME_SW_MGMT_OOB_IPV6_IF_CONFIG_SUCCESS = "SwMgmtOobIpv6IfConfigSuccess"
	CONST_NAME_SW_MGMT_OOB_IPV6_IF_CONFIG_SWITCH = "SwMgmtOobIpv6IfConfigSwitch"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
