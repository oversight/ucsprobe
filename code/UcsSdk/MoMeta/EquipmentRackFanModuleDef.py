import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentRackFanModuleDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentRackFanModuleDef")

	@staticmethod
	def ClassId():
		return "equipmentRackFanModuleDef"

	DESCR = "Descr"
	DN = "Dn"
	FAN_CAPACITY = "FanCapacity"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
