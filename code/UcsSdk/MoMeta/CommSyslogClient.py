import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommSyslogClient(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommSyslogClient")

	@staticmethod
	def ClassId():
		return "commSyslogClient"

	ADMIN_STATE = "AdminState"
	DN = "Dn"
	FORWARDING_FACILITY = "ForwardingFacility"
	HOSTNAME = "Hostname"
	NAME = "Name"
	RN = "Rn"
	SEVERITY = "Severity"
	STATUS = "Status"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_FORWARDING_FACILITY_LOCAL0 = "local0"
	CONST_FORWARDING_FACILITY_LOCAL1 = "local1"
	CONST_FORWARDING_FACILITY_LOCAL2 = "local2"
	CONST_FORWARDING_FACILITY_LOCAL3 = "local3"
	CONST_FORWARDING_FACILITY_LOCAL4 = "local4"
	CONST_FORWARDING_FACILITY_LOCAL5 = "local5"
	CONST_FORWARDING_FACILITY_LOCAL6 = "local6"
	CONST_FORWARDING_FACILITY_LOCAL7 = "local7"
	CONST_NAME_PRIMARY = "primary"
	CONST_NAME_SECONDARY = "secondary"
	CONST_NAME_TERTIARY = "tertiary"
	CONST_SEVERITY_ALERTS = "alerts"
	CONST_SEVERITY_CRITICAL = "critical"
	CONST_SEVERITY_DEBUGGING = "debugging"
	CONST_SEVERITY_EMERGENCIES = "emergencies"
	CONST_SEVERITY_ERRORS = "errors"
	CONST_SEVERITY_INFORMATION = "information"
	CONST_SEVERITY_NOTIFICATIONS = "notifications"
	CONST_SEVERITY_WARNINGS = "warnings"
