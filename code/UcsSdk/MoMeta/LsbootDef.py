import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsbootDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsbootDef")

	@staticmethod
	def ClassId():
		return "lsbootDef"

	ADV_BOOT_ORDER_APPLICABLE = "AdvBootOrderApplicable"
	BOOT_MODE = "BootMode"
	DESCR = "Descr"
	DN = "Dn"
	ENFORCE_VNIC_NAME = "EnforceVnicName"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PURPOSE = "Purpose"
	REBOOT_ON_UPDATE = "RebootOnUpdate"
	RN = "Rn"
	STATUS = "Status"

	CONST_ADV_BOOT_ORDER_APPLICABLE_FALSE = "false"
	CONST_ADV_BOOT_ORDER_APPLICABLE_NO = "no"
	CONST_ADV_BOOT_ORDER_APPLICABLE_TRUE = "true"
	CONST_ADV_BOOT_ORDER_APPLICABLE_YES = "yes"
	CONST_BOOT_MODE_LEGACY = "legacy"
	CONST_BOOT_MODE_UEFI = "uefi"
	CONST_ENFORCE_VNIC_NAME_FALSE = "false"
	CONST_ENFORCE_VNIC_NAME_NO = "no"
	CONST_ENFORCE_VNIC_NAME_TRUE = "true"
	CONST_ENFORCE_VNIC_NAME_YES = "yes"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PURPOSE_OPERATIONAL = "operational"
	CONST_PURPOSE_UTILITY = "utility"
	CONST_REBOOT_ON_UPDATE_FALSE = "false"
	CONST_REBOOT_ON_UPDATE_NO = "no"
	CONST_REBOOT_ON_UPDATE_TRUE = "true"
	CONST_REBOOT_ON_UPDATE_YES = "yes"
