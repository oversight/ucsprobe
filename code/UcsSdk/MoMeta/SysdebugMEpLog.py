import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysdebugMEpLog(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysdebugMEpLog")

	@staticmethod
	def ClassId():
		return "sysdebugMEpLog"

	ADMIN_STATE = "AdminState"
	CAPACITY = "Capacity"
	DN = "Dn"
	ID = "Id"
	LAST_UPDATE = "LastUpdate"
	OPER_STATE = "OperState"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_ADMIN_STATE_BACKUP = "backup"
	CONST_ADMIN_STATE_CLEAR = "clear"
	CONST_ADMIN_STATE_POLICY = "policy"
	CONST_CAPACITY_AVAILABLE = "available"
	CONST_CAPACITY_FULL = "full"
	CONST_CAPACITY_LOW = "low"
	CONST_CAPACITY_UNKNOWN = "unknown"
	CONST_CAPACITY_VERY_LOW = "very-low"
	CONST_LAST_UPDATE_NEVER = "never"
	CONST_OPER_STATE_BMC_COMMUNICATION_ERROR = "bmc-communication-error"
	CONST_OPER_STATE_INTERNAL_UCSM_ERROR = "internal-ucsm-error"
	CONST_OPER_STATE_OK = "ok"
	CONST_OPER_STATE_PERMISSION_DENIED_ERROR = "permission-denied-error"
	CONST_OPER_STATE_REMOTE_COMMUNICATION_ERROR = "remote-communication-error"
	CONST_TYPE_OBFL = "OBFL"
	CONST_TYPE_SEL = "SEL"
	CONST_TYPE_SYSLOG = "Syslog"
