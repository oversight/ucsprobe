import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentIOCardFsmTask(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentIOCardFsmTask")

	@staticmethod
	def ClassId():
		return "equipmentIOCardFsmTask"

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
	CONST_ITEM_FE_CONN = "FeConn"
	CONST_ITEM_FE_PRESENCE = "FePresence"
	CONST_ITEM_RESET_CMC = "ResetCmc"
	CONST_ITEM_RESET_IOM = "ResetIom"
	CONST_ITEM_MUX_OFFLINE = "muxOffline"
	CONST_ITEM_NOP = "nop"
