import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentLocalDiskControllerDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentLocalDiskControllerDef")

	@staticmethod
	def ClassId():
		return "equipmentLocalDiskControllerDef"

	DESCR = "Descr"
	DN = "Dn"
	FORCE_UPDATE_VERSION = "ForceUpdateVersion"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_FORCE_UPDATE_VERSION_FALSE = "false"
	CONST_FORCE_UPDATE_VERSION_NO = "no"
	CONST_FORCE_UPDATE_VERSION_TRUE = "true"
	CONST_FORCE_UPDATE_VERSION_YES = "yes"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
