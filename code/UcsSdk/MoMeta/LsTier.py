import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsTier(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsTier")

	@staticmethod
	def ClassId():
		return "lsTier"

	APPLY = "Apply"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SRC_TEMPL_NAME = "SrcTemplName"
	STATUS = "Status"

	CONST_APPLY_ON_ASSOCIATION = "onAssociation"
	CONST_APPLY_RUN_TIME = "runTime"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
