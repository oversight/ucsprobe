import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricVsan(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricVsan")

	@staticmethod
	def ClassId():
		return "fabricVsan"

	DEFAULT_ZONING = "DefaultZoning"
	DN = "Dn"
	EP_DN = "EpDn"
	FC_ZONE_SHARING_MODE = "FcZoneSharingMode"
	FCOE_VLAN = "FcoeVlan"
	GLOBAL = "Global"
	ID = "Id"
	IF_ROLE = "IfRole"
	IF_TYPE = "IfType"
	LOCAL = "Local"
	LOCALE = "Locale"
	NAME = "Name"
	OPER_STATE = "OperState"
	PEER_DN = "PeerDn"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"
	ZONING_STATE = "ZoningState"

	CONST_DEFAULT_ZONING_DISABLED = "disabled"
	CONST_DEFAULT_ZONING_ENABLED = "enabled"
	CONST_FC_ZONE_SHARING_MODE_CLEAR_UNMANAGED_ZONE_ALL = "clear-unmanaged-zone-all"
	CONST_FC_ZONE_SHARING_MODE_COALESCE = "coalesce"
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
	CONST_OPER_STATE_ERROR_RESERVED = "error-reserved"
	CONST_OPER_STATE_OK = "ok"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_SWITCH_ID_DUAL = "dual"
	CONST_ZONING_STATE_DISABLED = "disabled"
	CONST_ZONING_STATE_ENABLED = "enabled"
