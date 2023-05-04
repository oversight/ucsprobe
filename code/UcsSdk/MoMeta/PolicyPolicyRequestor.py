import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PolicyPolicyRequestor(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PolicyPolicyRequestor")

	@staticmethod
	def ClassId():
		return "policyPolicyRequestor"

	DN = "Dn"
	NAME = "Name"
	ON_BEHALF_OF_IDENT = "OnBehalfOfIdent"
	ON_BEHALF_OF_TYPE = "OnBehalfOfType"
	RESOLVED_CLASS_TYPE = "ResolvedClassType"
	RN = "Rn"
	STATUS = "Status"

