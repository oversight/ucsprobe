import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StatsThrFloatValue(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StatsThrFloatValue")

	@staticmethod
	def ClassId():
		return "statsThrFloatValue"

	DEESCALATING = "Deescalating"
	DESCR = "Descr"
	DIRECTION = "Direction"
	DN = "Dn"
	ESCALATING = "Escalating"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PROP_TYPE = "PropType"
	RN = "Rn"
	SEVERITY = "Severity"
	STATUS = "Status"

	CONST_DIRECTION_ABOVE_NORMAL = "aboveNormal"
	CONST_DIRECTION_BELOW_NORMAL = "belowNormal"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PROP_TYPE_FLOAT = "float"
	CONST_PROP_TYPE_UINT32 = "uint32"
	CONST_PROP_TYPE_UINT64 = "uint64"
	CONST_SEVERITY_CLEARED = "cleared"
	CONST_SEVERITY_CONDITION = "condition"
	CONST_SEVERITY_CRITICAL = "critical"
	CONST_SEVERITY_INFO = "info"
	CONST_SEVERITY_MAJOR = "major"
	CONST_SEVERITY_MINOR = "minor"
	CONST_SEVERITY_WARNING = "warning"
