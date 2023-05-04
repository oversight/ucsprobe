import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentServiceDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentServiceDef")

	@staticmethod
	def ClassId():
		return "equipmentServiceDef"

	CAN_BE_FRUED = "CanBeFRUed"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	REMOVAL_CONDITIONS = "RemovalConditions"
	RN = "Rn"
	SERVICE_PHILOSOPHY = "ServicePhilosophy"
	STATUS = "Status"

	CONST_CAN_BE_FRUED_FALSE = "false"
	CONST_CAN_BE_FRUED_NO = "no"
	CONST_CAN_BE_FRUED_TRUE = "true"
	CONST_CAN_BE_FRUED_YES = "yes"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_REMOVAL_CONDITIONS_NOT_APPLICABLE = "Not Applicable"
	CONST_REMOVAL_CONDITIONS_REMOVABLE_WHEN_OFF = "Removable when off"
	CONST_REMOVAL_CONDITIONS_REMOVABLE_WHEN_ON_OR_OFF = "Removable when on or off"
	CONST_REMOVAL_CONDITIONS_UNKNOWN = "Unknown"
