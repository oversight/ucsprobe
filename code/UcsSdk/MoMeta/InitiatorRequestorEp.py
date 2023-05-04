import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class InitiatorRequestorEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"InitiatorRequestorEp")

	@staticmethod
	def ClassId():
		return "initiatorRequestorEp"

	ALLOC_STATE = "AllocState"
	DN = "Dn"
	EP_DN = "EpDn"
	ID = "Id"
	RN = "Rn"
	STATUS = "Status"
	SYS_ID = "SysId"
	SYS_NAME = "SysName"

	CONST_ALLOC_STATE_ALLOCATED = "allocated"
	CONST_ALLOC_STATE_ALLOCATING = "allocating"
	CONST_ALLOC_STATE_FAILED = "failed"
	CONST_ALLOC_STATE_NONE = "none"
