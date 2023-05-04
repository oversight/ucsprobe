import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IppoolPool(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IppoolPool")

	@staticmethod
	def ClassId():
		return "ippoolPool"

	ASSIGNED = "Assigned"
	ASSIGNMENT_ORDER = "AssignmentOrder"
	DESCR = "Descr"
	DN = "Dn"
	EXT_MANAGED = "ExtManaged"
	GUID = "Guid"
	IS_NET_BIOSENABLED = "IsNetBIOSEnabled"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SIZE = "Size"
	STATUS = "Status"
	SUPPORTS_DHCP = "SupportsDHCP"
	V4_ASSIGNED = "V4Assigned"
	V4_SIZE = "V4Size"
	V6_ASSIGNED = "V6Assigned"
	V6_SIZE = "V6Size"

	CONST_ASSIGNMENT_ORDER_DEFAULT = "default"
	CONST_ASSIGNMENT_ORDER_SEQUENTIAL = "sequential"
	CONST_EXT_MANAGED_EXTERNAL = "external"
	CONST_EXT_MANAGED_INTERNAL = "internal"
	CONST_INT_ID_NONE = "none"
	CONST_IS_NET_BIOSENABLED_DISABLED = "disabled"
	CONST_IS_NET_BIOSENABLED_ENABLED = "enabled"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SUPPORTS_DHCP_DISABLED = "disabled"
	CONST_SUPPORTS_DHCP_ENABLED = "enabled"
