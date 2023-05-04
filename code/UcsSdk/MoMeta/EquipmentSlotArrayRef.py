import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentSlotArrayRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentSlotArrayRef")

	@staticmethod
	def ClassId():
		return "equipmentSlotArrayRef"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	NUMBER_OF_SLOTS_SPANNED = "NumberOfSlotsSpanned"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SLOT_SPAN_ORIENTATION = "SlotSpanOrientation"
	STATUS = "Status"
	TARGET_DN = "TargetDn"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SLOT_SPAN_ORIENTATION_INLINE = "inline"
	CONST_SLOT_SPAN_ORIENTATION_TRANSVERSE = "transverse"
	CONST_SLOT_SPAN_ORIENTATION_UNKNOWN = "unknown"
