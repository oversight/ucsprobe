import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricEthVlanPortEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricEthVlanPortEp")

	@staticmethod
	def ClassId():
		return "fabricEthVlanPortEp"

	ADMIN_STATE = "AdminState"
	CHASSIS_ID = "ChassisId"
	DN = "Dn"
	EP_DN = "EpDn"
	IF_ROLE = "IfRole"
	IF_TYPE = "IfType"
	IS_NATIVE = "IsNative"
	LIC_GP = "LicGP"
	LIC_STATE = "LicState"
	LOCALE = "Locale"
	NAME = "Name"
	OPER_STATE = "OperState"
	OPER_STATE_REASON = "OperStateReason"
	PEER_CHASSIS_ID = "PeerChassisId"
	PEER_DN = "PeerDn"
	PEER_PORT_ID = "PeerPortId"
	PEER_SLOT_ID = "PeerSlotId"
	PORT_ID = "PortId"
	RN = "Rn"
	SLOT_ID = "SlotId"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"
	WARNINGS = "Warnings"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_CHASSIS_ID_N_A = "N/A"
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
	CONST_IS_NATIVE_FALSE = "false"
	CONST_IS_NATIVE_NO = "no"
	CONST_IS_NATIVE_TRUE = "true"
	CONST_IS_NATIVE_YES = "yes"
	CONST_LIC_STATE_LICENSE_EXPIRED = "license-expired"
	CONST_LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
	CONST_LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
	CONST_LIC_STATE_LICENSE_OK = "license-ok"
	CONST_LIC_STATE_NOT_APPLICABLE = "not-applicable"
	CONST_LIC_STATE_UNKNOWN = "unknown"
	CONST_OPER_STATE_DOWN = "down"
	CONST_OPER_STATE_ERROR_MISCONFIGURED = "error-misconfigured"
	CONST_OPER_STATE_UNKNOWN = "unknown"
	CONST_OPER_STATE_UP = "up"
	CONST_PEER_CHASSIS_ID_N_A = "N/A"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
