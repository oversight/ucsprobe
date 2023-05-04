import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentChassisFsmTask(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentChassisFsmTask")

	@staticmethod
	def ClassId():
		return "equipmentChassisFsmTask"

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
	CONST_ITEM_DYNAMIC_REALLOCATION = "DynamicReallocation"
	CONST_ITEM_POWER_CAP = "PowerCap"
	CONST_ITEM_PSU_POLICY_CONFIG = "PsuPolicyConfig"
	CONST_ITEM_REMOVE_CHASSIS = "RemoveChassis"
	CONST_ITEM_NOP = "nop"
