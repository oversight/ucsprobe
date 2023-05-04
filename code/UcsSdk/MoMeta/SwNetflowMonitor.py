import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwNetflowMonitor(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwNetflowMonitor")

	@staticmethod
	def ClassId():
		return "swNetflowMonitor"

	ACTIVE_TIMEOUT = "ActiveTimeout"
	ADMIN_STATE = "AdminState"
	DN = "Dn"
	FLOW_RECORD_DEF_NAME = "FlowRecordDefName"
	INACTIVE_TIMEOUT = "InactiveTimeout"
	IS_VALID_CONFIG = "IsValidConfig"
	LIFE_CYCLE = "LifeCycle"
	NAME = "Name"
	PEER_DN = "PeerDn"
	PROTOCOL = "Protocol"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_IS_VALID_CONFIG_INCOMPLETE = "incomplete"
	CONST_IS_VALID_CONFIG_OK = "ok"
	CONST_LIFE_CYCLE_DELETED = "deleted"
	CONST_LIFE_CYCLE_NEW = "new"
	CONST_LIFE_CYCLE_NORMAL = "normal"
	CONST_PROTOCOL_NETFLOW = "netflow"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
