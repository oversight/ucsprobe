import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PolicyDiscovery(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PolicyDiscovery")

	@staticmethod
	def ClassId():
		return "policyDiscovery"

	DN = "Dn"
	RN = "Rn"
	SOURCE = "Source"
	STATUS = "Status"

	CONST_SOURCE_LOCAL = "local"
	CONST_SOURCE_PENDING_POLICY = "pending-policy"
	CONST_SOURCE_POLICY = "policy"
