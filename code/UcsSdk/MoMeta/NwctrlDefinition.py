import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class NwctrlDefinition(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"NwctrlDefinition")

	@staticmethod
	def ClassId():
		return "nwctrlDefinition"

	CDP = "Cdp"
	DESCR = "Descr"
	DN = "Dn"
	MAC_REGISTER_MODE = "MacRegisterMode"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	UPLINK_FAIL_ACTION = "UplinkFailAction"

	CONST_CDP_DISABLED = "disabled"
	CONST_CDP_ENABLED = "enabled"
	CONST_INT_ID_NONE = "none"
	CONST_MAC_REGISTER_MODE_ALL_HOST_VLANS = "all-host-vlans"
	CONST_MAC_REGISTER_MODE_ONLY_NATIVE_VLAN = "only-native-vlan"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_UPLINK_FAIL_ACTION_LINK_DOWN = "link-down"
	CONST_UPLINK_FAIL_ACTION_WARNING = "warning"
