import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeBladeDiscPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeBladeDiscPolicy")

	@staticmethod
	def ClassId():
		return "computeBladeDiscPolicy"

	ACTION = "Action"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	QUALIFIER = "Qualifier"
	RN = "Rn"
	SCRUB_POLICY_NAME = "ScrubPolicyName"
	STATUS = "Status"

	CONST_ACTION_DIAG = "diag"
	CONST_ACTION_IMMEDIATE = "immediate"
	CONST_ACTION_USER_ACKNOWLEDGED = "user-acknowledged"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
