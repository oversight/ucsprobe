import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwFcoeSanPc(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwFcoeSanPc")

	@staticmethod
	def ClassId():
		return "swFcoeSanPc"

	ADMIN_STATE = "AdminState"
	DN = "Dn"
	EP_DN = "EpDn"
	IF_ROLE = "IfRole"
	IF_TYPE = "IfType"
	LACP_FAST_TIMER = "LacpFastTimer"
	LACP_SUSPEND_INDIVIDUAL = "LacpSuspendIndividual"
	LOCALE = "Locale"
	MON_TRAF_DIR = "MonTrafDir"
	NAME = "Name"
	PC_ID = "PcId"
	PEER_DN = "PeerDn"
	PEER_STATE = "PeerState"
	PORT_ID = "PortId"
	PORT_VSAN_ID = "PortVsanId"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"

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
	CONST_LACP_FAST_TIMER_FALSE = "false"
	CONST_LACP_FAST_TIMER_NO = "no"
	CONST_LACP_FAST_TIMER_TRUE = "true"
	CONST_LACP_FAST_TIMER_YES = "yes"
	CONST_LACP_SUSPEND_INDIVIDUAL_FALSE = "false"
	CONST_LACP_SUSPEND_INDIVIDUAL_NO = "no"
	CONST_LACP_SUSPEND_INDIVIDUAL_TRUE = "true"
	CONST_LACP_SUSPEND_INDIVIDUAL_YES = "yes"
	CONST_MON_TRAF_DIR_BOTH = "both"
	CONST_MON_TRAF_DIR_RX = "rx"
	CONST_MON_TRAF_DIR_TX = "tx"
	CONST_PEER_STATE_EXISTING = "existing"
	CONST_PEER_STATE_NONEXISTING = "nonexisting"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
