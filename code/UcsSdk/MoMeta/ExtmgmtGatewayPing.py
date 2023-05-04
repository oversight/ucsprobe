import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtmgmtGatewayPing(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtmgmtGatewayPing")

	@staticmethod
	def ClassId():
		return "extmgmtGatewayPing"

	DN = "Dn"
	MAX_DEADLINE_TIMEOUT = "MaxDeadlineTimeout"
	NUMBER_OF_PING_REQUESTS = "NumberOfPingRequests"
	RN = "Rn"
	STATUS = "Status"

