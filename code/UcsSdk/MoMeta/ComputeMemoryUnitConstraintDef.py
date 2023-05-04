import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeMemoryUnitConstraintDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeMemoryUnitConstraintDef")

	@staticmethod
	def ClassId():
		return "computeMemoryUnitConstraintDef"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	REVISION_MODIFIER = "RevisionModifier"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_TYPE_KIT = "kit"
	CONST_TYPE_UNKNOWN = "unknown"
