import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePsuPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePsuPolicy")

	@staticmethod
	def ClassId():
		return "computePsuPolicy"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	REDUNDANCY = "Redundancy"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_REDUNDANCY_GRID = "grid"
	CONST_REDUNDANCY_N_1 = "n+1"
	CONST_REDUNDANCY_NON_REDUNDANT = "non-redundant"
