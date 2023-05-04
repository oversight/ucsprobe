import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtIfFsmTask(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtIfFsmTask")

	@staticmethod
	def ClassId():
		return "mgmtIfFsmTask"

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
	CONST_ITEM_DISABLE_VIP = "DisableVip"
	CONST_ITEM_ENABLE_HA = "EnableHA"
	CONST_ITEM_ENABLE_VIP = "EnableVip"
	CONST_ITEM_SW_MGMT_INBAND_IF_CONFIG = "SwMgmtInbandIfConfig"
	CONST_ITEM_SW_MGMT_OOB_IF_CONFIG = "SwMgmtOobIfConfig"
	CONST_ITEM_VIRTUAL_IF_CONFIG = "VirtualIfConfig"
	CONST_ITEM_NOP = "nop"
