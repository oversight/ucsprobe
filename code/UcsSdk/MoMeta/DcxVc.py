import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DcxVc(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DcxVc")

	@staticmethod
	def ClassId():
		return "dcxVc"

	ADMIN_STATE = "AdminState"
	BORDER_PORT_ID = "BorderPortId"
	BORDER_SLOT_ID = "BorderSlotId"
	BORDER_VFC_ID = "BorderVfcId"
	CDP = "Cdp"
	COOKIE = "Cookie"
	COS = "Cos"
	DERIVED_FROM_ID = "DerivedFromId"
	DN = "Dn"
	ENCAP = "Encap"
	FCOE_ID = "FcoeId"
	FORGE_MAC = "ForgeMac"
	ID = "Id"
	INST_TYPE = "InstType"
	LC = "Lc"
	LINK_STATE = "LinkState"
	LOCALE = "Locale"
	MAC_REGISTER_MODE = "MacRegisterMode"
	MON_TRAF_DIR = "MonTrafDir"
	NAME = "Name"
	OPER_BORDER_PORT_ID = "OperBorderPortId"
	OPER_BORDER_SLOT_ID = "OperBorderSlotId"
	OPER_STATE = "OperState"
	PEER_ID = "PeerId"
	PROT_STATE = "ProtState"
	QOS_POLICY_DN = "QosPolicyDn"
	QOS_POLICY_ID = "QosPolicyId"
	RN = "Rn"
	ROLE = "Role"
	STATE = "State"
	STATE_QUAL = "StateQual"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TAG = "Tag"
	TRANSPORT = "Transport"
	TYPE = "Type"
	UPLINK_FAIL_ACTION = "UplinkFailAction"
	VNIC = "Vnic"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_CDP_DISABLED = "disabled"
	CONST_CDP_ENABLED = "enabled"
	CONST_COS_ANY = "any"
	CONST_ENCAP_CONSOLIDATED = "consolidated"
	CONST_ENCAP_VIRTUAL = "virtual"
	CONST_FORGE_MAC_ALLOW = "allow"
	CONST_FORGE_MAC_DENY = "deny"
	CONST_INST_TYPE_DEFAULT = "default"
	CONST_INST_TYPE_DYNAMIC = "dynamic"
	CONST_INST_TYPE_DYNAMIC_VF = "dynamic-vf"
	CONST_INST_TYPE_MANUAL = "manual"
	CONST_LC_ALLOCATED = "allocated"
	CONST_LC_AVAILABLE = "available"
	CONST_LC_DEALLOCATED = "deallocated"
	CONST_LC_REPURPOSED = "repurposed"
	CONST_LINK_STATE_ADMIN_DOWN = "admin-down"
	CONST_LINK_STATE_DOWN = "down"
	CONST_LINK_STATE_ERROR = "error"
	CONST_LINK_STATE_UNALLOCATED = "unallocated"
	CONST_LINK_STATE_UNAVAILABLE = "unavailable"
	CONST_LINK_STATE_UNKNOWN = "unknown"
	CONST_LINK_STATE_UP = "up"
	CONST_MAC_REGISTER_MODE_ALL_HOST_VLANS = "all-host-vlans"
	CONST_MAC_REGISTER_MODE_ONLY_NATIVE_VLAN = "only-native-vlan"
	CONST_MON_TRAF_DIR_BOTH = "both"
	CONST_MON_TRAF_DIR_RX = "rx"
	CONST_MON_TRAF_DIR_TX = "tx"
	CONST_OPER_STATE_ACTIVE = "active"
	CONST_OPER_STATE_ADMIN_DOWN = "admin-down"
	CONST_OPER_STATE_ERROR = "error"
	CONST_OPER_STATE_LINK_DOWN = "link-down"
	CONST_OPER_STATE_PASSIVE = "passive"
	CONST_OPER_STATE_UNKNOWN = "unknown"
	CONST_PROT_STATE_ACTIVE = "active"
	CONST_PROT_STATE_NO_PROTECTION = "no-protection"
	CONST_PROT_STATE_PASSIVE = "passive"
	CONST_QOS_POLICY_ID_NONE = "none"
	CONST_ROLE_DIAG = "diag"
	CONST_ROLE_FCOE_NAS_STORAGE = "fcoe-nas-storage"
	CONST_ROLE_FCOE_STORAGE = "fcoe-storage"
	CONST_ROLE_FCOE_UPLINK = "fcoe-uplink"
	CONST_ROLE_MGMT = "mgmt"
	CONST_ROLE_MONITOR = "monitor"
	CONST_ROLE_NAS_STORAGE = "nas-storage"
	CONST_ROLE_NETWORK = "network"
	CONST_ROLE_NETWORK_FCOE_UPLINK = "network-fcoe-uplink"
	CONST_ROLE_SERVER = "server"
	CONST_ROLE_SERVICE = "service"
	CONST_ROLE_STORAGE = "storage"
	CONST_ROLE_UNKNOWN = "unknown"
	CONST_STATE_CREATE_PEND = "CreatePend"
	CONST_STATE_CREATING = "Creating"
	CONST_STATE_DESTROY_PEND = "DestroyPend"
	CONST_STATE_DESTROYING = "Destroying"
	CONST_STATE_MODIFY_PEND = "ModifyPend"
	CONST_STATE_MODIFYING = "Modifying"
	CONST_STATE_PRESENT = "Present"
	CONST_STATE_UNKNOWN = "Unknown"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_UPLINK_FAIL_ACTION_LINK_DOWN = "link-down"
	CONST_UPLINK_FAIL_ACTION_WARNING = "warning"
