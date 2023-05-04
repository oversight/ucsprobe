import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PolicyElement(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PolicyElement")

	@staticmethod
	def ClassId():
		return "policyElement"

	CLASS_TYPE = "ClassType"
	CONVERTED_DN = "ConvertedDn"
	DN = "Dn"
	OWNERSHIP = "Ownership"
	POLICY_DN = "PolicyDn"
	RN = "Rn"
	STATUS = "Status"

	CONST_OWNERSHIP_LOCAL = "local"
	CONST_OWNERSHIP_PENDING_POLICY = "pending-policy"
	CONST_OWNERSHIP_POLICY = "policy"
