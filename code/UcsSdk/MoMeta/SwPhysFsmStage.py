import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwPhysFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwPhysFsmStage")

	@staticmethod
	def ClassId():
		return "swPhysFsmStage"

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
	CONST_NAME_CONF_PHYSICAL_BEGIN = "ConfPhysicalBegin"
	CONST_NAME_CONF_PHYSICAL_CONFIG_SW_A = "ConfPhysicalConfigSwA"
	CONST_NAME_CONF_PHYSICAL_CONFIG_SW_B = "ConfPhysicalConfigSwB"
	CONST_NAME_CONF_PHYSICAL_FAIL = "ConfPhysicalFail"
	CONST_NAME_CONF_PHYSICAL_PORT_INVENTORY_SW_A = "ConfPhysicalPortInventorySwA"
	CONST_NAME_CONF_PHYSICAL_PORT_INVENTORY_SW_B = "ConfPhysicalPortInventorySwB"
	CONST_NAME_CONF_PHYSICAL_SUCCESS = "ConfPhysicalSuccess"
	CONST_NAME_CONF_PHYSICAL_VERIFY_PHYS_CONFIG = "ConfPhysicalVerifyPhysConfig"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
