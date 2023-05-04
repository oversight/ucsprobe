import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VmSwitch(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VmSwitch")

	@staticmethod
	def ClassId():
		return "vmSwitch"

	ADMIN_STATE = "AdminState"
	DESCR = "Descr"
	DN = "Dn"
	EXT_KEY = "ExtKey"
	ID = "Id"
	KEY_INST = "KeyInst"
	MANAGER = "Manager"
	NAME = "Name"
	OWN = "Own"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	UUID = "Uuid"
	VENDOR = "Vendor"

	CONST_ADMIN_STATE_DISABLE = "disable"
	CONST_ADMIN_STATE_ENABLE = "enable"
	CONST_INT_ID_NONE = "none"
	CONST_MANAGER_RHEV_M = "rhev-m"
	CONST_MANAGER_SCVMM = "scvmm"
	CONST_MANAGER_UNMANAGED = "unmanaged"
	CONST_MANAGER_VCENTER = "vcenter"
	CONST_OWN_DISCOVERED = "discovered"
	CONST_OWN_MANAGED = "managed"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_VENDOR_MICROSOFT = "microsoft"
	CONST_VENDOR_UNDETERMINED = "undetermined"
	CONST_VENDOR_VMWARE = "vmware"
