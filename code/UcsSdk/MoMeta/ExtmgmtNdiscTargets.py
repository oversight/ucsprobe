import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtmgmtNdiscTargets(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtmgmtNdiscTargets")

	@staticmethod
	def ClassId():
		return "extmgmtNdiscTargets"

	CONFIG_STATE = "ConfigState"
	CONFIG_STATUS_MESSAGE = "ConfigStatusMessage"
	DN = "Dn"
	IPV6_TARGET1 = "Ipv6Target1"
	IPV6_TARGET2 = "Ipv6Target2"
	IPV6_TARGET3 = "Ipv6Target3"
	MAX_DEADLINE_TIMEOUT = "MaxDeadlineTimeout"
	NUMBER_OF_NDISC_REQUESTS = "NumberOfNdiscRequests"
	RN = "Rn"
	STATUS = "Status"

	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_CONFIG_STATE_OK = "ok"
