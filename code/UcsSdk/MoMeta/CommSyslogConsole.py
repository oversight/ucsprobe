import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommSyslogConsole(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommSyslogConsole")

	@staticmethod
	def ClassId():
		return "commSyslogConsole"

	ADMIN_STATE = "AdminState"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	SEVERITY = "Severity"
	STATUS = "Status"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_SEVERITY_ALERTS = "alerts"
	CONST_SEVERITY_CRITICAL = "critical"
	CONST_SEVERITY_EMERGENCIES = "emergencies"
