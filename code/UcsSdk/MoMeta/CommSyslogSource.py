import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommSyslogSource(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommSyslogSource")

	@staticmethod
	def ClassId():
		return "commSyslogSource"

	AUDITS = "Audits"
	DESCR = "Descr"
	DN = "Dn"
	EVENTS = "Events"
	FAULTS = "Faults"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

	CONST_AUDITS_DISABLED = "disabled"
	CONST_AUDITS_ENABLED = "enabled"
	CONST_EVENTS_DISABLED = "disabled"
	CONST_EVENTS_ENABLED = "enabled"
	CONST_FAULTS_DISABLED = "disabled"
	CONST_FAULTS_ENABLED = "enabled"
