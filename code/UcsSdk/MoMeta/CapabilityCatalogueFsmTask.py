import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CapabilityCatalogueFsmTask(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CapabilityCatalogueFsmTask")

	@staticmethod
	def ClassId():
		return "capabilityCatalogueFsmTask"

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
	CONST_ITEM_ACTIVATE_CATALOG = "ActivateCatalog"
	CONST_ITEM_DEPLOY_CATALOGUE = "DeployCatalogue"
	CONST_ITEM_NOP = "nop"
