import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwFcSanPc(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwFcSanPc")

	@staticmethod
	def ClassId():
		return "swFcSanPc"

	ADMIN_SPEED = "AdminSpeed"
	ADMIN_STATE = "AdminState"
	DN = "Dn"
	EP_DN = "EpDn"
	IF_ROLE = "IfRole"
	IF_TYPE = "IfType"
	LOCALE = "Locale"
	MON_TRAF_DIR = "MonTrafDir"
	NAME = "Name"
	PC_ID = "PcId"
	PEER_DN = "PeerDn"
	PORT_ID = "PortId"
	PORT_VSAN_ID = "PortVsanId"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_ADMIN_SPEED_1GBPS = "1gbps"
	CONST_ADMIN_SPEED_2GBPS = "2gbps"
	CONST_ADMIN_SPEED_4GBPS = "4gbps"
	CONST_ADMIN_SPEED_8GBPS = "8gbps"
	CONST_ADMIN_SPEED_AUTO = "auto"
	CONST_ADMIN_SPEED_INDETERMINATE = "indeterminate"
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
	CONST_MON_TRAF_DIR_BOTH = "both"
	CONST_MON_TRAF_DIR_RX = "rx"
	CONST_MON_TRAF_DIR_TX = "tx"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
