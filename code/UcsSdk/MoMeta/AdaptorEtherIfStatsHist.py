import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEtherIfStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEtherIfStatsHist")

	@staticmethod
	def ClassId():
		return "adaptorEtherIfStatsHist"

	DN = "Dn"
	ID = "Id"
	MOST_RECENT = "MostRecent"
	RN = "Rn"
	RX_BYTES = "RxBytes"
	RX_BYTES_DELTA = "RxBytesDelta"
	RX_BYTES_DELTA_AVG = "RxBytesDeltaAvg"
	RX_BYTES_DELTA_MAX = "RxBytesDeltaMax"
	RX_BYTES_DELTA_MIN = "RxBytesDeltaMin"
	RX_DROPPED = "RxDropped"
	RX_DROPPED_DELTA = "RxDroppedDelta"
	RX_DROPPED_DELTA_AVG = "RxDroppedDeltaAvg"
	RX_DROPPED_DELTA_MAX = "RxDroppedDeltaMax"
	RX_DROPPED_DELTA_MIN = "RxDroppedDeltaMin"
	RX_ERRORS = "RxErrors"
	RX_ERRORS_DELTA = "RxErrorsDelta"
	RX_ERRORS_DELTA_AVG = "RxErrorsDeltaAvg"
	RX_ERRORS_DELTA_MAX = "RxErrorsDeltaMax"
	RX_ERRORS_DELTA_MIN = "RxErrorsDeltaMin"
	RX_PACKETS = "RxPackets"
	RX_PACKETS_DELTA = "RxPacketsDelta"
	RX_PACKETS_DELTA_AVG = "RxPacketsDeltaAvg"
	RX_PACKETS_DELTA_MAX = "RxPacketsDeltaMax"
	RX_PACKETS_DELTA_MIN = "RxPacketsDeltaMin"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TX_BYTES = "TxBytes"
	TX_BYTES_DELTA = "TxBytesDelta"
	TX_BYTES_DELTA_AVG = "TxBytesDeltaAvg"
	TX_BYTES_DELTA_MAX = "TxBytesDeltaMax"
	TX_BYTES_DELTA_MIN = "TxBytesDeltaMin"
	TX_DROPPED = "TxDropped"
	TX_DROPPED_DELTA = "TxDroppedDelta"
	TX_DROPPED_DELTA_AVG = "TxDroppedDeltaAvg"
	TX_DROPPED_DELTA_MAX = "TxDroppedDeltaMax"
	TX_DROPPED_DELTA_MIN = "TxDroppedDeltaMin"
	TX_ERRORS = "TxErrors"
	TX_ERRORS_DELTA = "TxErrorsDelta"
	TX_ERRORS_DELTA_AVG = "TxErrorsDeltaAvg"
	TX_ERRORS_DELTA_MAX = "TxErrorsDeltaMax"
	TX_ERRORS_DELTA_MIN = "TxErrorsDeltaMin"
	TX_PACKETS = "TxPackets"
	TX_PACKETS_DELTA = "TxPacketsDelta"
	TX_PACKETS_DELTA_AVG = "TxPacketsDeltaAvg"
	TX_PACKETS_DELTA_MAX = "TxPacketsDeltaMax"
	TX_PACKETS_DELTA_MIN = "TxPacketsDeltaMin"

	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
