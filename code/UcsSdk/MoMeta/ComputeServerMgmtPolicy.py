import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeServerMgmtPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeServerMgmtPolicy")

	@staticmethod
	def ClassId():
		return "computeServerMgmtPolicy"

	ACTION = "Action"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	QUALIFIER = "Qualifier"
	RN = "Rn"
	STATUS = "Status"

	CONST_ACTION_AUTO_ACKNOWLEDGED = "auto-acknowledged"
	CONST_ACTION_USER_ACKNOWLEDGED = "user-acknowledged"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
