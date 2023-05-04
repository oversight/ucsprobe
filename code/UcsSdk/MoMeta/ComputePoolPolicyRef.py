import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePoolPolicyRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePoolPolicyRef")

	@staticmethod
	def ClassId():
		return "computePoolPolicyRef"

	DN = "Dn"
	ID = "Id"
	POLICY_DN = "PolicyDn"
	RN = "Rn"
	STATUS = "Status"

