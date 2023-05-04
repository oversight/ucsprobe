import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricLacpPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricLacpPolicy")

	@staticmethod
	def ClassId():
		return "fabricLacpPolicy"

	DESCR = "Descr"
	DN = "Dn"
	FAST_TIMER = "FastTimer"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	SUSPEND_INDIVIDUAL = "SuspendIndividual"

	CONST_FAST_TIMER_FAST = "fast"
	CONST_FAST_TIMER_NORMAL = "normal"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SUSPEND_INDIVIDUAL_FALSE = "false"
	CONST_SUSPEND_INDIVIDUAL_TRUE = "true"
