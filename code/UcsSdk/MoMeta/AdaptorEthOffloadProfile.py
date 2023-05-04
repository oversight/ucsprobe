import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEthOffloadProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEthOffloadProfile")

	@staticmethod
	def ClassId():
		return "adaptorEthOffloadProfile"

	DN = "Dn"
	LARGE_RECEIVE = "LargeReceive"
	RN = "Rn"
	STATUS = "Status"
	TCP_RX_CHECKSUM = "TcpRxChecksum"
	TCP_SEGMENT = "TcpSegment"
	TCP_TX_CHECKSUM = "TcpTxChecksum"

	CONST_LARGE_RECEIVE_DISABLED = "disabled"
	CONST_LARGE_RECEIVE_ENABLED = "enabled"
	CONST_TCP_RX_CHECKSUM_DISABLED = "disabled"
	CONST_TCP_RX_CHECKSUM_ENABLED = "enabled"
	CONST_TCP_SEGMENT_DISABLED = "disabled"
	CONST_TCP_SEGMENT_ENABLED = "enabled"
	CONST_TCP_TX_CHECKSUM_DISABLED = "disabled"
	CONST_TCP_TX_CHECKSUM_ENABLED = "enabled"
