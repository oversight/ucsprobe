import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorIscsiProt(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorIscsiProt")

	@staticmethod
	def ClassId():
		return "adaptorIscsiProt"

	CONNECTION_TIME_OUT = "ConnectionTimeOut"
	DHCP_TIME_OUT = "DhcpTimeOut"
	DN = "Dn"
	INITIATOR_NAME = "InitiatorName"
	LUN_BUSY_RETRY_COUNT = "LunBusyRetryCount"
	RN = "Rn"
	STATUS = "Status"
	TCP_TIME_STAMP = "TcpTimeStamp"

	CONST_TCP_TIME_STAMP_FALSE = "false"
	CONST_TCP_TIME_STAMP_NO = "no"
	CONST_TCP_TIME_STAMP_TRUE = "true"
	CONST_TCP_TIME_STAMP_YES = "yes"
