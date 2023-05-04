import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicProfileSetFsmTask(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicProfileSetFsmTask")

	@staticmethod
	def ClassId():
		return "vnicProfileSetFsmTask"

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
	CONST_ITEM_DEPLOY = "Deploy"
	CONST_ITEM_DEPLOY_ALIAS = "DeployAlias"
	CONST_ITEM_NOP = "nop"
