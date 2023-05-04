import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricEthMon(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricEthMon")

	@staticmethod
	def ClassId():
		return "fabricEthMon"

	ADMIN_STATE = "AdminState"
	CONFIG_FAIL_REASON = "ConfigFailReason"
	DN = "Dn"
	ID = "Id"
	IS_CONFIG_SUCCESS = "IsConfigSuccess"
	LOCALE = "Locale"
	NAME = "Name"
	OPER_STATE = "OperState"
	OPER_STATE_REASON = "OperStateReason"
	PEER_DN = "PeerDn"
	RN = "Rn"
	SESSION = "Session"
	STATUS = "Status"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_ID_A = "A"
	CONST_ID_B = "B"
	CONST_ID_NONE = "NONE"
	CONST_IS_CONFIG_SUCCESS_FALSE = "false"
	CONST_IS_CONFIG_SUCCESS_NO = "no"
	CONST_IS_CONFIG_SUCCESS_TRUE = "true"
	CONST_IS_CONFIG_SUCCESS_YES = "yes"
	CONST_OPER_STATE_DOWN = "down"
	CONST_OPER_STATE_ERROR = "error"
	CONST_OPER_STATE_UNKNOWN = "unknown"
	CONST_OPER_STATE_UP = "up"
	CONST_OPER_STATE_REASON_ACTIVE = "Active"
	CONST_OPER_STATE_REASON_GENERIC_ERROR = "Generic_Error"
	CONST_OPER_STATE_REASON_NO_DESTINATION_CONFIGURED = "No_Destination_Configured"
	CONST_OPER_STATE_REASON_NO_FLOW_ID_SPECIFIED = "No_Flow-id_Specified"
	CONST_OPER_STATE_REASON_NO_HARDWARE_RESOURCE = "No_Hardware_Resource"
	CONST_OPER_STATE_REASON_NO_OPERATIONAL_SRC_DST = "No_Operational_Src_Dst"
	CONST_OPER_STATE_REASON_NO_SOURCE_DESTINATION_CONFIGURED = "No_Source_Destination_Configured"
	CONST_OPER_STATE_REASON_NO_SOURCES_CONFIGURED = "No_Sources_Configured"
	CONST_OPER_STATE_REASON_SESSION_ADMIN_SHUT = "Session_Admin_Shut"
	CONST_OPER_STATE_REASON_TUNNEL_MISCONF_DOWN = "Tunnel_Misconf_Down"
	CONST_OPER_STATE_REASON_UNKNOWN = "Unknown"
	CONST_OPER_STATE_REASON_WRONG_DESTINATION_MODE = "Wrong_Destination_Mode"
	CONST_OPER_STATE_REASON_WRONG_SOURCE_MODE = "Wrong_Source_Mode"
