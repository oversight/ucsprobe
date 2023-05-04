import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentMemoryUnitDiscoveryModifierDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentMemoryUnitDiscoveryModifierDef")

	@staticmethod
	def ClassId():
		return "equipmentMemoryUnitDiscoveryModifierDef"

	ACTION = "Action"
	CONSTRAINT_TYPE = "ConstraintType"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_ACTION_SET_REV = "setRev"
	CONST_ACTION_SET_REV_STRICT = "setRevStrict"
	CONST_ACTION_SET_REV_TO_ONE = "setRevToOne"
	CONST_ACTION_UNKNOWN = "unknown"
	CONST_CONSTRAINT_TYPE_KIT = "kit"
	CONST_CONSTRAINT_TYPE_UNKNOWN = "unknown"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
