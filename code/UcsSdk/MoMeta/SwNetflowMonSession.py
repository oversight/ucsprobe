import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwNetflowMonSession(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwNetflowMonSession")

	@staticmethod
	def ClassId():
		return "swNetflowMonSession"

	ADMIN_STATE = "AdminState"
	DN = "Dn"
	HAS_LAST_DEST = "HasLastDest"
	LIFE_CYCLE = "LifeCycle"
	NAME = "Name"
	PEER_DN = "PeerDn"
	PROTOCOL = "Protocol"
	RN = "Rn"
	SESSION = "Session"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_HAS_LAST_DEST_FALSE = "false"
	CONST_HAS_LAST_DEST_NO = "no"
	CONST_HAS_LAST_DEST_TRUE = "true"
	CONST_HAS_LAST_DEST_YES = "yes"
	CONST_LIFE_CYCLE_DELETED = "deleted"
	CONST_LIFE_CYCLE_NEW = "new"
	CONST_LIFE_CYCLE_NORMAL = "normal"
	CONST_PROTOCOL_NETFLOW = "netflow"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
