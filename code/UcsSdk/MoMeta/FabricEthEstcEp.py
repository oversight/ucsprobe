import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricEthEstcEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricEthEstcEp")

	@staticmethod
	def ClassId():
		return "fabricEthEstcEp"

	ADMIN_SPEED = "AdminSpeed"
	ADMIN_STATE = "AdminState"
	CHASSIS_ID = "ChassisId"
	CONFIG_STATE = "ConfigState"
	DN = "Dn"
	EP_DN = "EpDn"
	FLOW_CTRL_POLICY = "FlowCtrlPolicy"
	IF_ROLE = "IfRole"
	IF_TYPE = "IfType"
	LIC_GP = "LicGP"
	LIC_STATE = "LicState"
	LOCALE = "Locale"
	NAME = "Name"
	NW_CTRL_POLICY_NAME = "NwCtrlPolicyName"
	OPER_NW_CTRL_POLICY_NAME = "OperNwCtrlPolicyName"
	OPER_PORT_MODE = "OperPortMode"
	OPER_STATE = "OperState"
	OPER_STATE_REASON = "OperStateReason"
	PEER_CHASSIS_ID = "PeerChassisId"
	PEER_DN = "PeerDn"
	PEER_PORT_ID = "PeerPortId"
	PEER_SLOT_ID = "PeerSlotId"
	PIN_GROUP_NAME = "PinGroupName"
	PORT_ID = "PortId"
	PORT_MODE = "PortMode"
	PRIO = "Prio"
	RN = "Rn"
	SLOT_ID = "SlotId"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"
	USR_LBL = "UsrLbl"
	WARNINGS = "Warnings"

	CONST_ADMIN_SPEED_10GBPS = "10gbps"
	CONST_ADMIN_SPEED_1GBPS = "1gbps"
	CONST_ADMIN_SPEED_20GBPS = "20gbps"
	CONST_ADMIN_SPEED_40GBPS = "40gbps"
	CONST_ADMIN_SPEED_INDETERMINATE = "indeterminate"
	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_CHASSIS_ID_N_A = "N/A"
	CONST_CONFIG_STATE_APPLIED = "applied"
	CONST_CONFIG_STATE_INCONSISTENT = "inconsistent"
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
	CONST_LIC_STATE_LICENSE_EXPIRED = "license-expired"
	CONST_LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
	CONST_LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
	CONST_LIC_STATE_LICENSE_OK = "license-ok"
	CONST_LIC_STATE_NOT_APPLICABLE = "not-applicable"
	CONST_LIC_STATE_UNKNOWN = "unknown"
	CONST_OPER_PORT_MODE_PROMISCUOUS_ACCESS = "promiscuous access"
	CONST_OPER_PORT_MODE_PROMISCUOUS_TRUNK = "promiscuous trunk"
	CONST_OPER_PORT_MODE_REGULAR_ACCESS = "regular access"
	CONST_OPER_PORT_MODE_REGULAR_TRUNK = "regular trunk"
	CONST_OPER_STATE_DOWN = "down"
	CONST_OPER_STATE_ERROR_MISCONFIGURED = "error-misconfigured"
	CONST_OPER_STATE_UNKNOWN = "unknown"
	CONST_OPER_STATE_UP = "up"
	CONST_PEER_CHASSIS_ID_N_A = "N/A"
	CONST_PORT_MODE_ACCESS = "access"
	CONST_PORT_MODE_TRUNK = "trunk"
	CONST_PRIO_BEST_EFFORT = "best-effort"
	CONST_PRIO_BRONZE = "bronze"
	CONST_PRIO_FC = "fc"
	CONST_PRIO_GOLD = "gold"
	CONST_PRIO_PLATINUM = "platinum"
	CONST_PRIO_SILVER = "silver"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
