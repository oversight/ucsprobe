import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeAutoconfigPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeAutoconfigPolicy")

	@staticmethod
	def ClassId():
		return "computeAutoconfigPolicy"

	DESCR = "Descr"
	DN = "Dn"
	DST_DN = "DstDn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	QUALIFIER = "Qualifier"
	RN = "Rn"
	SRC_TEMPL_NAME = "SrcTemplName"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
