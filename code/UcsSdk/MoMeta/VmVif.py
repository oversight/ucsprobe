import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VmVif(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VmVif")

	@staticmethod
	def ClassId():
		return "vmVif"

	ADP_VIF_ID = "AdpVifId"
	COOKIE = "Cookie"
	DN = "Dn"
	LINK_STATE = "LinkState"
	OPER_STATE = "OperState"
	PH_SWITCH_ID = "PhSwitchId"
	PHS_ACCESS_CARD_ID = "PhsAccessCardId"
	PHS_ACCESS_PORT_ID = "PhsAccessPortId"
	PHS_BORDER_CARD_ID = "PhsBorderCardId"
	PHS_BORDER_PORT_ID = "PhsBorderPortId"
	RN = "Rn"
	STATE_QUAL = "StateQual"
	STATUS = "Status"
	STATUS_CHANGE_TS = "StatusChangeTs"
	V_STATUS = "VStatus"
	VC_DN = "VcDn"
	VIF_ID = "VifId"

	CONST_LINK_STATE_ADMIN_DOWN = "admin-down"
	CONST_LINK_STATE_DOWN = "down"
	CONST_LINK_STATE_ERROR = "error"
	CONST_LINK_STATE_UNALLOCATED = "unallocated"
	CONST_LINK_STATE_UNAVAILABLE = "unavailable"
	CONST_LINK_STATE_UNKNOWN = "unknown"
	CONST_LINK_STATE_UP = "up"
	CONST_OPER_STATE_ACTIVE = "active"
	CONST_OPER_STATE_ADMIN_DOWN = "admin-down"
	CONST_OPER_STATE_ERROR = "error"
	CONST_OPER_STATE_LINK_DOWN = "link-down"
	CONST_OPER_STATE_PASSIVE = "passive"
	CONST_OPER_STATE_UNKNOWN = "unknown"
	CONST_PH_SWITCH_ID_A = "A"
	CONST_PH_SWITCH_ID_B = "B"
	CONST_PH_SWITCH_ID_NONE = "NONE"
	CONST_V_STATUS_OFFLINE = "offline"
	CONST_V_STATUS_ONLINE = "online"
	CONST_V_STATUS_UNKNOWN = "unknown"
