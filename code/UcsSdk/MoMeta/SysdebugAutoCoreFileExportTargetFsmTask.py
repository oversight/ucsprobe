import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysdebugAutoCoreFileExportTargetFsmTask(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysdebugAutoCoreFileExportTargetFsmTask")

	@staticmethod
	def ClassId():
		return "sysdebugAutoCoreFileExportTargetFsmTask"

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
	CONST_ITEM_CONFIGURE = "Configure"
	CONST_ITEM_NOP = "nop"
