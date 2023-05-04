import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PowerGroupAdditionPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PowerGroupAdditionPolicy")

	@staticmethod
	def ClassId():
		return "powerGroupAdditionPolicy"

	ACTION = "Action"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_ACTION_NOTHING = "nothing"
	CONST_ACTION_STOP_BLADE_DISC = "stop-blade-disc"
	CONST_ACTION_THROTTLE_BLADE_DISC = "throttle-blade-disc"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
