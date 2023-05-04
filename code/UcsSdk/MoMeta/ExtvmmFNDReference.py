import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtvmmFNDReference(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtvmmFNDReference")

	@staticmethod
	def ClassId():
		return "extvmmFNDReference"

	DESCR = "Descr"
	DN = "Dn"
	FN_DEF_NAME = "FnDefName"
	NAME = "Name"
	OPER_FN_DEF_NAME = "OperFnDefName"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
