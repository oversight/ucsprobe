import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtmgmtMiiStatus(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtmgmtMiiStatus")

	@staticmethod
	def ClassId():
		return "extmgmtMiiStatus"

	DN = "Dn"
	MAX_RETRY_COUNT = "MaxRetryCount"
	RETRY_INTERVAL = "RetryInterval"
	RN = "Rn"
	STATUS = "Status"

