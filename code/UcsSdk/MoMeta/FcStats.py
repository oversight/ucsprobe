import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FcStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FcStats")

	@staticmethod
	def ClassId():
		return "fcStats"

	BYTES_RX = "BytesRx"
	BYTES_RX_DELTA = "BytesRxDelta"
	BYTES_RX_DELTA_AVG = "BytesRxDeltaAvg"
	BYTES_RX_DELTA_MAX = "BytesRxDeltaMax"
	BYTES_RX_DELTA_MIN = "BytesRxDeltaMin"
	BYTES_TX = "BytesTx"
	BYTES_TX_DELTA = "BytesTxDelta"
	BYTES_TX_DELTA_AVG = "BytesTxDeltaAvg"
	BYTES_TX_DELTA_MAX = "BytesTxDeltaMax"
	BYTES_TX_DELTA_MIN = "BytesTxDeltaMin"
	DN = "Dn"
	INTERVALS = "Intervals"
	PACKETS_RX = "PacketsRx"
	PACKETS_RX_DELTA = "PacketsRxDelta"
	PACKETS_RX_DELTA_AVG = "PacketsRxDeltaAvg"
	PACKETS_RX_DELTA_MAX = "PacketsRxDeltaMax"
	PACKETS_RX_DELTA_MIN = "PacketsRxDeltaMin"
	PACKETS_TX = "PacketsTx"
	PACKETS_TX_DELTA = "PacketsTxDelta"
	PACKETS_TX_DELTA_AVG = "PacketsTxDeltaAvg"
	PACKETS_TX_DELTA_MAX = "PacketsTxDeltaMax"
	PACKETS_TX_DELTA_MIN = "PacketsTxDeltaMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
