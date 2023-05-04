import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtControllerFsmTask(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtControllerFsmTask")

	@staticmethod
	def ClassId():
		return "mgmtControllerFsmTask"

	COMPLETION = "Completion"
	DN = "Dn"
	FLAGS = "Flags"
	ITEM = "Item"
	RN = "Rn"
	SEQ_ID = "SeqId"
	STATUS = "Status"

	CONST_COMPLETION_CANCELLED = "cancelled"
	CONST_COMPLETION_COMPLETED = "completed"
	CONST_COMPLETION_PROCESSING = "processing"
	CONST_COMPLETION_SCHEDULED = "scheduled"
	CONST_ITEM_ACTIVATE_BMC = "ActivateBMC"
	CONST_ITEM_ACTIVATE_IOM = "ActivateIOM"
	CONST_ITEM_EXT_MGMT_IF_CONFIG = "ExtMgmtIfConfig"
	CONST_ITEM_EXT_MGMT_INTERFACE_CONFIG = "ExtMgmtInterfaceConfig"
	CONST_ITEM_ONLINE = "Online"
	CONST_ITEM_REGISTRY_CONFIG = "RegistryConfig"
	CONST_ITEM_SYS_CONFIG = "SysConfig"
	CONST_ITEM_UPDATE_BMC = "UpdateBMC"
	CONST_ITEM_UPDATE_IOM = "UpdateIOM"
	CONST_ITEM_UPDATE_SWITCH = "UpdateSwitch"
	CONST_ITEM_UPDATE_UCSMANAGER = "UpdateUCSManager"
	CONST_ITEM_NOP = "nop"
