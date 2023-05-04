import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicProfile")

	@staticmethod
	def ClassId():
		return "vnicProfile"

	CDP = "Cdp"
	CONFIG_QUALIFIER = "ConfigQualifier"
	COS = "Cos"
	DESCR = "Descr"
	DN = "Dn"
	FORGE_MAC = "ForgeMac"
	HOST_NW_IOPERF = "HostNwIOPerf"
	MAC_REGISTER_MODE = "MacRegisterMode"
	MAX_PORTS = "MaxPorts"
	NAME = "Name"
	NW_CTRL_POLICY_NAME = "NwCtrlPolicyName"
	OPER_NW_CTRL_POLICY_NAME = "OperNwCtrlPolicyName"
	OPER_QOS_POLICY_NAME = "OperQosPolicyName"
	PIN_TO_GROUP_NAME = "PinToGroupName"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PORT_PROFILE_UUID = "PortProfileUuid"
	PRIMARY_VLAN_ID = "PrimaryVlanId"
	QOS_POLICY_DN = "QosPolicyDn"
	QOS_POLICY_ID = "QosPolicyId"
	QOS_POLICY_NAME = "QosPolicyName"
	RN = "Rn"
	STATUS = "Status"
	SW_ABORDER_PORT = "SwABorderPort"
	SW_ABORDER_SLOT = "SwABorderSlot"
	SW_BBORDER_PORT = "SwBBorderPort"
	SW_BBORDER_SLOT = "SwBBorderSlot"
	TYPE = "Type"
	UPLINK_FAIL_ACTION = "UplinkFailAction"

	CONST_CDP_DISABLED = "disabled"
	CONST_CDP_ENABLED = "enabled"
	CONST_CONFIG_QUALIFIER_INVALID_NAME = "invalid-name"
	CONST_CONFIG_QUALIFIER_NORMAL = "normal"
	CONST_COS_ANY = "any"
	CONST_FORGE_MAC_ALLOW = "allow"
	CONST_FORGE_MAC_DENY = "deny"
	CONST_HOST_NW_IOPERF_HIGH_PERF_REQD = "high-perf-reqd"
	CONST_HOST_NW_IOPERF_NONE = "none"
	CONST_INT_ID_NONE = "none"
	CONST_MAC_REGISTER_MODE_ALL_HOST_VLANS = "all-host-vlans"
	CONST_MAC_REGISTER_MODE_ONLY_NATIVE_VLAN = "only-native-vlan"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_QOS_POLICY_ID_NONE = "none"
	CONST_TYPE_REGULAR = "regular"
	CONST_TYPE_SLA_ONLY = "sla-only"
	CONST_UPLINK_FAIL_ACTION_LINK_DOWN = "link-down"
	CONST_UPLINK_FAIL_ACTION_WARNING = "warning"
