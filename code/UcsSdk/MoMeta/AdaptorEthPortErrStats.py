import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEthPortErrStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEthPortErrStats")

	@staticmethod
	def ClassId():
		return "adaptorEthPortErrStats"

	BAD_CRC_PACKETS = "BadCrcPackets"
	BAD_CRC_PACKETS_DELTA = "BadCrcPacketsDelta"
	BAD_CRC_PACKETS_DELTA_AVG = "BadCrcPacketsDeltaAvg"
	BAD_CRC_PACKETS_DELTA_MAX = "BadCrcPacketsDeltaMax"
	BAD_CRC_PACKETS_DELTA_MIN = "BadCrcPacketsDeltaMin"
	BAD_LENGTH_PACKETS = "BadLengthPackets"
	BAD_LENGTH_PACKETS_DELTA = "BadLengthPacketsDelta"
	BAD_LENGTH_PACKETS_DELTA_AVG = "BadLengthPacketsDeltaAvg"
	BAD_LENGTH_PACKETS_DELTA_MAX = "BadLengthPacketsDeltaMax"
	BAD_LENGTH_PACKETS_DELTA_MIN = "BadLengthPacketsDeltaMin"
	DN = "Dn"
	INTERVALS = "Intervals"
	MAC_DISCARDED_PACKETS = "MacDiscardedPackets"
	MAC_DISCARDED_PACKETS_DELTA = "MacDiscardedPacketsDelta"
	MAC_DISCARDED_PACKETS_DELTA_AVG = "MacDiscardedPacketsDeltaAvg"
	MAC_DISCARDED_PACKETS_DELTA_MAX = "MacDiscardedPacketsDeltaMax"
	MAC_DISCARDED_PACKETS_DELTA_MIN = "MacDiscardedPacketsDeltaMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TRAFFIC_DIRECTION = "TrafficDirection"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
	CONST_TRAFFIC_DIRECTION_RX = "rx"
	CONST_TRAFFIC_DIRECTION_TX = "tx"
	CONST_TRAFFIC_DIRECTION_UNKNOWN = "unknown"
