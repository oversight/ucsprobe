import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PolicyRefReq(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PolicyRefReq")

	@staticmethod
	def ClassId():
		return "policyRefReq"

	DN = "Dn"
	POLICY_OWNER = "PolicyOwner"
	REF_CONVERTED_DN = "RefConvertedDn"
	REF_POLICY_DN = "RefPolicyDn"
	RN = "Rn"
	STATUS = "Status"

	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
