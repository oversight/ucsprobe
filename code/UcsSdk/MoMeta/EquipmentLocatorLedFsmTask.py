import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentLocatorLedFsmTask(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentLocatorLedFsmTask")

	@staticmethod
	def ClassId():
		return "equipmentLocatorLedFsmTask"

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
	CONST_ITEM_SET_FE_LOCATOR_LED = "SetFeLocatorLed"
	CONST_ITEM_SET_FI_LOCATOR_LED = "SetFiLocatorLed"
	CONST_ITEM_SET_LOCATOR_LED = "SetLocatorLed"
	CONST_ITEM_NOP = "nop"
