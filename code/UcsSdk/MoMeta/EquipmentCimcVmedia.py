import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentCimcVmedia(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentCimcVmedia")

	@staticmethod
	def ClassId():
		return "equipmentCimcVmedia"

	DESCR = "Descr"
	DN = "Dn"
	IS_SUPPORTED = "IsSupported"
	MIN_BIOS_VERSION = "MinBiosVersion"
	MIN_CIMC_VERSION = "MinCimcVersion"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_IS_SUPPORTED_FALSE = "false"
	CONST_IS_SUPPORTED_NO = "no"
	CONST_IS_SUPPORTED_TRUE = "true"
	CONST_IS_SUPPORTED_YES = "yes"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
