import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommSyslog(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommSyslog")

	@staticmethod
	def ClassId():
		return "commSyslog"

	ADMIN_STATE = "AdminState"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	OPER_PORT = "OperPort"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PORT = "Port"
	PROTO = "Proto"
	RN = "Rn"
	SEVERITY = "Severity"
	STATUS = "Status"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PROTO_ALL = "all"
	CONST_PROTO_NONE = "none"
	CONST_PROTO_TCP = "tcp"
	CONST_PROTO_UDP = "udp"
	CONST_SEVERITY_ALERTS = "alerts"
	CONST_SEVERITY_CRITICAL = "critical"
	CONST_SEVERITY_DEBUGGING = "debugging"
	CONST_SEVERITY_EMERGENCIES = "emergencies"
	CONST_SEVERITY_ERRORS = "errors"
	CONST_SEVERITY_INFORMATION = "information"
	CONST_SEVERITY_NOTIFICATIONS = "notifications"
	CONST_SEVERITY_WARNINGS = "warnings"
