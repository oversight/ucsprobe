import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwEthLanBorderFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwEthLanBorderFsmStage")

	@staticmethod
	def ClassId():
		return "swEthLanBorderFsmStage"

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
	CONST_NAME_DEPLOY_BEGIN = "DeployBegin"
	CONST_NAME_DEPLOY_FAIL = "DeployFail"
	CONST_NAME_DEPLOY_SUCCESS = "DeploySuccess"
	CONST_NAME_DEPLOY_UPDATE_CONNECTIVITY = "DeployUpdateConnectivity"
	CONST_NAME_DEPLOY_UPDATE_VLAN_GROUPS = "DeployUpdateVlanGroups"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
