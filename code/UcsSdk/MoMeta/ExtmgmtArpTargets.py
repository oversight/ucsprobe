import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtmgmtArpTargets(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtmgmtArpTargets")

	@staticmethod
	def ClassId():
		return "extmgmtArpTargets"

	CONFIG_STATE = "ConfigState"
	CONFIG_STATUS_MESSAGE = "ConfigStatusMessage"
	DN = "Dn"
	MAX_DEADLINE_TIMEOUT = "MaxDeadlineTimeout"
	NUMBER_OF_ARP_REQUESTS = "NumberOfArpRequests"
	RN = "Rn"
	STATUS = "Status"
	TARGET_IP1 = "TargetIp1"
	TARGET_IP2 = "TargetIp2"
	TARGET_IP3 = "TargetIp3"

	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_CONFIG_STATE_OK = "ok"
