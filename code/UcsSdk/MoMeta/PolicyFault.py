import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PolicyFault(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PolicyFault")

	@staticmethod
	def ClassId():
		return "policyFault"

	DN = "Dn"
	RN = "Rn"
	SOURCE = "Source"
	STATUS = "Status"

	CONST_SOURCE_LOCAL = "local"
	CONST_SOURCE_PENDING_POLICY = "pending-policy"
	CONST_SOURCE_POLICY = "policy"
