import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPortGroupSwComplexDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPortGroupSwComplexDef")

	@staticmethod
	def ClassId():
		return "equipmentPortGroupSwComplexDef"

	ASIC = "Asic"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PORT_CAPACITY = "PortCapacity"
	RN = "Rn"
	STATUS = "Status"
	SW_COMPLEX_CAPACITY = "SwComplexCapacity"
	VIF_CAPACITY = "VifCapacity"

	CONST_ASIC_CARMEL = "carmel"
	CONST_ASIC_GATOS = "gatos"
	CONST_ASIC_UNKNOWN = "unknown"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
