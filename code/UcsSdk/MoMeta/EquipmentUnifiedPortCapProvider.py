import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentUnifiedPortCapProvider(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentUnifiedPortCapProvider")

	@staticmethod
	def ClassId():
		return "equipmentUnifiedPortCapProvider"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	SUPPORTED_ALGORITHM = "SupportedAlgorithm"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SUPPORTED_ALGORITHM_NONE = "none"
	CONST_SUPPORTED_ALGORITHM_SLIDE_RULE = "slide-rule"
	CONST_SUPPORTED_ALGORITHM_UNRESTRICTED = "unrestricted"
