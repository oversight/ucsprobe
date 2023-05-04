import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPortSwComplexRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPortSwComplexRef")

	@staticmethod
	def ClassId():
		return "equipmentPortSwComplexRef"

	DESCR = "Descr"
	DN = "Dn"
	MAX_PORT_ID = "MaxPortId"
	MIN_PORT_ID = "MinPortId"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SLOT_ID = "SlotId"
	STATUS = "Status"
	SW_COMPLEX_ID = "SwComplexId"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
