import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEthPortOutsizedStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEthPortOutsizedStats")

	@staticmethod
	def ClassId():
		return "adaptorEthPortOutsizedStats"

	DN = "Dn"
	INTERVALS = "Intervals"
	OVERSIZED_BAD_CRC_PACKETS = "OversizedBadCrcPackets"
	OVERSIZED_BAD_CRC_PACKETS_DELTA = "OversizedBadCrcPacketsDelta"
	OVERSIZED_BAD_CRC_PACKETS_DELTA_AVG = "OversizedBadCrcPacketsDeltaAvg"
	OVERSIZED_BAD_CRC_PACKETS_DELTA_MAX = "OversizedBadCrcPacketsDeltaMax"
	OVERSIZED_BAD_CRC_PACKETS_DELTA_MIN = "OversizedBadCrcPacketsDeltaMin"
	OVERSIZED_GOOD_CRC_PACKETS = "OversizedGoodCrcPackets"
	OVERSIZED_GOOD_CRC_PACKETS_DELTA = "OversizedGoodCrcPacketsDelta"
	OVERSIZED_GOOD_CRC_PACKETS_DELTA_AVG = "OversizedGoodCrcPacketsDeltaAvg"
	OVERSIZED_GOOD_CRC_PACKETS_DELTA_MAX = "OversizedGoodCrcPacketsDeltaMax"
	OVERSIZED_GOOD_CRC_PACKETS_DELTA_MIN = "OversizedGoodCrcPacketsDeltaMin"
	OVERSIZED_PACKETS = "OversizedPackets"
	OVERSIZED_PACKETS_DELTA = "OversizedPacketsDelta"
	OVERSIZED_PACKETS_DELTA_AVG = "OversizedPacketsDeltaAvg"
	OVERSIZED_PACKETS_DELTA_MAX = "OversizedPacketsDeltaMax"
	OVERSIZED_PACKETS_DELTA_MIN = "OversizedPacketsDeltaMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TRAFFIC_DIRECTION = "TrafficDirection"
	UNDERSIZED_BAD_CRC_PACKETS = "UndersizedBadCrcPackets"
	UNDERSIZED_BAD_CRC_PACKETS_DELTA = "UndersizedBadCrcPacketsDelta"
	UNDERSIZED_BAD_CRC_PACKETS_DELTA_AVG = "UndersizedBadCrcPacketsDeltaAvg"
	UNDERSIZED_BAD_CRC_PACKETS_DELTA_MAX = "UndersizedBadCrcPacketsDeltaMax"
	UNDERSIZED_BAD_CRC_PACKETS_DELTA_MIN = "UndersizedBadCrcPacketsDeltaMin"
	UNDERSIZED_GOOD_CRC_PACKETS = "UndersizedGoodCrcPackets"
	UNDERSIZED_GOOD_CRC_PACKETS_DELTA = "UndersizedGoodCrcPacketsDelta"
	UNDERSIZED_GOOD_CRC_PACKETS_DELTA_AVG = "UndersizedGoodCrcPacketsDeltaAvg"
	UNDERSIZED_GOOD_CRC_PACKETS_DELTA_MAX = "UndersizedGoodCrcPacketsDeltaMax"
	UNDERSIZED_GOOD_CRC_PACKETS_DELTA_MIN = "UndersizedGoodCrcPacketsDeltaMin"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
	CONST_TRAFFIC_DIRECTION_RX = "rx"
	CONST_TRAFFIC_DIRECTION_TX = "tx"
	CONST_TRAFFIC_DIRECTION_UNKNOWN = "unknown"
