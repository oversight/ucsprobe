import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtmgmtIf(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtmgmtIf")

	@staticmethod
	def ClassId():
		return "extmgmtIf"

	DN = "Dn"
	EP_DN = "EpDn"
	FAIL_REPORT_COUNT = "FailReportCount"
	ID = "Id"
	IF_ROLE = "IfRole"
	IF_TYPE = "IfType"
	LAST_OPER_STATE_REPORT = "LastOperStateReport"
	LOCALE = "Locale"
	NAME = "Name"
	OPER_STATE = "OperState"
	PEER_DN = "PeerDn"
	RN = "Rn"
	STATUS = "Status"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_ID_A = "A"
	CONST_ID_B = "B"
	CONST_ID_NONE = "NONE"
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
	CONST_LAST_OPER_STATE_REPORT_DOWN = "down"
	CONST_LAST_OPER_STATE_REPORT_UNKNOWN = "unknown"
	CONST_LAST_OPER_STATE_REPORT_UP = "up"
	CONST_OPER_STATE_DOWN = "down"
	CONST_OPER_STATE_UNKNOWN = "unknown"
	CONST_OPER_STATE_UP = "up"
