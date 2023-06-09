import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VmVlan(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VmVlan")

	@staticmethod
	def ClassId():
		return "vmVlan"

	ASSOC_PRIMARY_VLAN_STATE = "AssocPrimaryVlanState"
	ASSOC_PRIMARY_VLAN_SWITCH_ID = "AssocPrimaryVlanSwitchId"
	DN = "Dn"
	EP_DN = "EpDn"
	ID = "Id"
	IF_ROLE = "IfRole"
	IF_TYPE = "IfType"
	LOCALE = "Locale"
	NAME = "Name"
	OPER_STATE = "OperState"
	OVERLAP_STATE_FOR_A = "OverlapStateForA"
	OVERLAP_STATE_FOR_B = "OverlapStateForB"
	PEER_DN = "PeerDn"
	POLICY_OWNER = "PolicyOwner"
	PUB_NW_DN = "PubNwDn"
	PUB_NW_ID = "PubNwId"
	PUB_NW_NAME = "PubNwName"
	RN = "Rn"
	SHARING = "Sharing"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_ASSOC_PRIMARY_VLAN_STATE_DOES_NOT_EXISTS = "does-not-exists"
	CONST_ASSOC_PRIMARY_VLAN_STATE_IS_EMPTY = "is-empty"
	CONST_ASSOC_PRIMARY_VLAN_STATE_IS_IN_ERROR_STATE = "is-in-error-state"
	CONST_ASSOC_PRIMARY_VLAN_STATE_IS_NOT_PRIMARY_TYPE = "is-not-primary-type"
	CONST_ASSOC_PRIMARY_VLAN_STATE_OK = "ok"
	CONST_ASSOC_PRIMARY_VLAN_SWITCH_ID_A = "A"
	CONST_ASSOC_PRIMARY_VLAN_SWITCH_ID_B = "B"
	CONST_ASSOC_PRIMARY_VLAN_SWITCH_ID_NONE = "NONE"
	CONST_IF_ROLE_DIAG = "diag"
	CONST_IF_ROLE_FCOE_NAS_STORAGE = "fcoe-nas-storage"
	CONST_IF_ROLE_FCOE_STORAGE = "fcoe-storage"
	CONST_IF_ROLE_FCOE_UPLINK = "fcoe-uplink"
	CONST_IF_ROLE_MGMT = "mgmt"
	CONST_IF_ROLE_MONITOR = "monitor"
	CONST_IF_ROLE_NAS_STORAGE = "nas-storage"
	CONST_IF_ROLE_NETWORK = "network"
	CONST_IF_ROLE_NETWORK_FCOE_UPLINK = "network-fcoe-uplink"
	CONST_IF_ROLE_SERVER = "server"
	CONST_IF_ROLE_SERVICE = "service"
	CONST_IF_ROLE_STORAGE = "storage"
	CONST_IF_ROLE_UNKNOWN = "unknown"
	CONST_IF_TYPE_AGGREGATION = "aggregation"
	CONST_IF_TYPE_PHYSICAL = "physical"
	CONST_IF_TYPE_UNKNOWN = "unknown"
	CONST_IF_TYPE_VIRTUAL = "virtual"
	CONST_OPER_STATE_ERROR_MISCONFIGURED = "error-misconfigured"
	CONST_OPER_STATE_OK = "ok"
	CONST_OVERLAP_STATE_FOR_A_NOT_ACTIVE = "not-active"
	CONST_OVERLAP_STATE_FOR_A_OK = "ok"
	CONST_OVERLAP_STATE_FOR_A_PRIMARY_ID_MISMATCH = "primary-id-mismatch"
	CONST_OVERLAP_STATE_FOR_A_SHARING_TYPE_MISMATCH = "sharing-type-mismatch"
	CONST_OVERLAP_STATE_FOR_B_NOT_ACTIVE = "not-active"
	CONST_OVERLAP_STATE_FOR_B_OK = "ok"
	CONST_OVERLAP_STATE_FOR_B_PRIMARY_ID_MISMATCH = "primary-id-mismatch"
	CONST_OVERLAP_STATE_FOR_B_SHARING_TYPE_MISMATCH = "sharing-type-mismatch"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SHARING_COMMUNITY = "community"
	CONST_SHARING_ISOLATED = "isolated"
	CONST_SHARING_NONE = "none"
	CONST_SHARING_PRIMARY = "primary"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
