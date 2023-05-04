import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class InitiatorRequestorGrpEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"InitiatorRequestorGrpEp")

	@staticmethod
	def ClassId():
		return "initiatorRequestorGrpEp"

	ALLOC_STATE = "AllocState"
	DN = "Dn"
	EP_DN = "EpDn"
	ID = "Id"
	LC = "Lc"
	POL_DN = "PolDn"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_ALLOC_STATE_ALLOCATED = "allocated"
	CONST_ALLOC_STATE_ALLOCATING = "allocating"
	CONST_ALLOC_STATE_FAILED = "failed"
	CONST_ALLOC_STATE_NONE = "none"
	CONST_LC_ALLOCATED = "allocated"
	CONST_LC_AVAILABLE = "available"
	CONST_LC_DEALLOCATED = "deallocated"
	CONST_LC_REPURPOSED = "repurposed"
	CONST_TYPE_DEDICATED = "dedicated"
	CONST_TYPE_POLICY = "policy"
	CONST_TYPE_SHARED = "shared"
