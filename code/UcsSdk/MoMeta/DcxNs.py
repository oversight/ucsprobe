import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DcxNs(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DcxNs")

	@staticmethod
	def ClassId():
		return "dcxNs"

	ALLOC_STATUS = "AllocStatus"
	DN = "Dn"
	RN = "Rn"
	SIDE = "Side"
	SIZE = "Size"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	USED = "Used"

	CONST_ALLOC_STATUS_AVAILABLE = "available"
	CONST_ALLOC_STATUS_EXCEEDED = "exceeded"
	CONST_ALLOC_STATUS_FULL = "full"
	CONST_SIDE_LEFT = "left"
	CONST_SIDE_RIGHT = "right"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
