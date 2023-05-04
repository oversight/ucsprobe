import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentBladeConnDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentBladeConnDef")

	@staticmethod
	def ClassId():
		return "equipmentBladeConnDef"

	ADAPTOR_FAMILY = "AdaptorFamily"
	ADAPTOR_SLOT_NUMBER = "AdaptorSlotNumber"
	ADAPTOR_SLOT_SPAN = "AdaptorSlotSpan"
	ADAPTOR_TYPE = "AdaptorType"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	PARENT_ADAPTOR_SLOT_NUM = "ParentAdaptorSlotNum"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_PORT_MUX_OFFSET = "SwitchPortMuxOffset"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
