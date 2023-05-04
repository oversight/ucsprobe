import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EtherRxStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EtherRxStatsHist")

	@staticmethod
	def ClassId():
		return "etherRxStatsHist"

	BROADCAST_PACKETS = "BroadcastPackets"
	BROADCAST_PACKETS_DELTA = "BroadcastPacketsDelta"
	BROADCAST_PACKETS_DELTA_AVG = "BroadcastPacketsDeltaAvg"
	BROADCAST_PACKETS_DELTA_MAX = "BroadcastPacketsDeltaMax"
	BROADCAST_PACKETS_DELTA_MIN = "BroadcastPacketsDeltaMin"
	DN = "Dn"
	ID = "Id"
	JUMBO_PACKETS = "JumboPackets"
	JUMBO_PACKETS_DELTA = "JumboPacketsDelta"
	JUMBO_PACKETS_DELTA_AVG = "JumboPacketsDeltaAvg"
	JUMBO_PACKETS_DELTA_MAX = "JumboPacketsDeltaMax"
	JUMBO_PACKETS_DELTA_MIN = "JumboPacketsDeltaMin"
	MOST_RECENT = "MostRecent"
	MULTICAST_PACKETS = "MulticastPackets"
	MULTICAST_PACKETS_DELTA = "MulticastPacketsDelta"
	MULTICAST_PACKETS_DELTA_AVG = "MulticastPacketsDeltaAvg"
	MULTICAST_PACKETS_DELTA_MAX = "MulticastPacketsDeltaMax"
	MULTICAST_PACKETS_DELTA_MIN = "MulticastPacketsDeltaMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TOTAL_BYTES = "TotalBytes"
	TOTAL_BYTES_DELTA = "TotalBytesDelta"
	TOTAL_BYTES_DELTA_AVG = "TotalBytesDeltaAvg"
	TOTAL_BYTES_DELTA_MAX = "TotalBytesDeltaMax"
	TOTAL_BYTES_DELTA_MIN = "TotalBytesDeltaMin"
	TOTAL_PACKETS = "TotalPackets"
	TOTAL_PACKETS_DELTA = "TotalPacketsDelta"
	TOTAL_PACKETS_DELTA_AVG = "TotalPacketsDeltaAvg"
	TOTAL_PACKETS_DELTA_MAX = "TotalPacketsDeltaMax"
	TOTAL_PACKETS_DELTA_MIN = "TotalPacketsDeltaMin"
	UNICAST_PACKETS = "UnicastPackets"
	UNICAST_PACKETS_DELTA = "UnicastPacketsDelta"
	UNICAST_PACKETS_DELTA_AVG = "UnicastPacketsDeltaAvg"
	UNICAST_PACKETS_DELTA_MAX = "UnicastPacketsDeltaMax"
	UNICAST_PACKETS_DELTA_MIN = "UnicastPacketsDeltaMin"

	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
