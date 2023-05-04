import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorVnicStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorVnicStatsHist")

	@staticmethod
	def ClassId():
		return "adaptorVnicStatsHist"

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
	DROPPED_RX = "DroppedRx"
	DROPPED_RX_DELTA = "DroppedRxDelta"
	DROPPED_RX_DELTA_AVG = "DroppedRxDeltaAvg"
	DROPPED_RX_DELTA_MAX = "DroppedRxDeltaMax"
	DROPPED_RX_DELTA_MIN = "DroppedRxDeltaMin"
	DROPPED_TX = "DroppedTx"
	DROPPED_TX_DELTA = "DroppedTxDelta"
	DROPPED_TX_DELTA_AVG = "DroppedTxDeltaAvg"
	DROPPED_TX_DELTA_MAX = "DroppedTxDeltaMax"
	DROPPED_TX_DELTA_MIN = "DroppedTxDeltaMin"
	ERRORS_RX = "ErrorsRx"
	ERRORS_RX_DELTA = "ErrorsRxDelta"
	ERRORS_RX_DELTA_AVG = "ErrorsRxDeltaAvg"
	ERRORS_RX_DELTA_MAX = "ErrorsRxDeltaMax"
	ERRORS_RX_DELTA_MIN = "ErrorsRxDeltaMin"
	ERRORS_TX = "ErrorsTx"
	ERRORS_TX_DELTA = "ErrorsTxDelta"
	ERRORS_TX_DELTA_AVG = "ErrorsTxDeltaAvg"
	ERRORS_TX_DELTA_MAX = "ErrorsTxDeltaMax"
	ERRORS_TX_DELTA_MIN = "ErrorsTxDeltaMin"
	ID = "Id"
	MOST_RECENT = "MostRecent"
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

	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
