import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProcStimulusCounts(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ProcStimulusCounts")

	@staticmethod
	def ClassId():
		return "procStimulusCounts"

	ADMIN_STATE = "AdminState"
	BULKED = "Bulked"
	DN = "Dn"
	FAILED = "Failed"
	RETRIED = "Retried"
	RN = "Rn"
	SINGLETON = "Singleton"
	STATUS = "Status"
	SUCCESSFULL = "Successfull"
	TOTAL = "Total"

	CONST_ADMIN_STATE_CLEAR_STATS = "clear-stats"
	CONST_ADMIN_STATE_LOG_STATS = "log-stats"
	CONST_ADMIN_STATE_ON = "on"
