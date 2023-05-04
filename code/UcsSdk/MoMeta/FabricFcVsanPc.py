import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricFcVsanPc(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricFcVsanPc")

	@staticmethod
	def ClassId():
		return "fabricFcVsanPc"

	ADMIN_STATE = "AdminState"
	DESCR = "Descr"
	DN = "Dn"
	EP_DN = "EpDn"
	IF_ROLE = "IfRole"
	IF_TYPE = "IfType"
	LOCALE = "Locale"
	NAME = "Name"
	OPER_STATE = "OperState"
	PEER_DN = "PeerDn"
	PORT_ID = "PortId"
	RN = "Rn"
	STATE_QUAL = "StateQual"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"
	WARNINGS = "Warnings"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
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
	CONST_OPER_STATE_ADMIN_DOWN = "admin-down"
	CONST_OPER_STATE_ERROR_DISABLED = "error-disabled"
	CONST_OPER_STATE_FAILED = "failed"
	CONST_OPER_STATE_HARDWARE_FAILURE = "hardware-failure"
	CONST_OPER_STATE_INDETERMINATE = "indeterminate"
	CONST_OPER_STATE_LINK_DOWN = "link-down"
	CONST_OPER_STATE_LINK_UP = "link-up"
	CONST_OPER_STATE_NO_LICENSE = "no-license"
	CONST_OPER_STATE_SFP_NOT_PRESENT = "sfp-not-present"
	CONST_OPER_STATE_SOFTWARE_FAILURE = "software-failure"
	CONST_OPER_STATE_UDLD_AGGR_DOWN = "udld-aggr-down"
	CONST_OPER_STATE_UP = "up"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
