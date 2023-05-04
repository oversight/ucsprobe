import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEthPortOutsizedStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEthPortOutsizedStatsHist")

	@staticmethod
	def ClassId():
		return "adaptorEthPortOutsizedStatsHist"

	DN = "Dn"
	ID = "Id"
	MOST_RECENT = "MostRecent"
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

	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
