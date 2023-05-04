import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeMemoryConfiguration(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeMemoryConfiguration")

	@staticmethod
	def ClassId():
		return "computeMemoryConfiguration"

	ADMIN_MEMORY_STATE = "AdminMemoryState"
	BLACK_LISTING = "BlackListing"
	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

	CONST_ADMIN_MEMORY_STATE_POLICY = "policy"
	CONST_ADMIN_MEMORY_STATE_RESET_IN_PROGRESS = "reset-in-progress"
	CONST_ADMIN_MEMORY_STATE_RESET_MEMORY_ERRORS = "reset-memory-errors"
	CONST_BLACK_LISTING_DISABLED = "disabled"
	CONST_BLACK_LISTING_ENABLED = "enabled"
