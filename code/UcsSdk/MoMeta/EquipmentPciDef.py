import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPciDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPciDef")

	@staticmethod
	def ClassId():
		return "equipmentPciDef"

	DESCR = "Descr"
	DEVICE = "Device"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	SUBDEVICE = "Subdevice"
	SUBVENDOR = "Subvendor"
	VENDOR = "Vendor"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
