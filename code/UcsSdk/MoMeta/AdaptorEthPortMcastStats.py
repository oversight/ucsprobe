import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEthPortMcastStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEthPortMcastStats")

	@staticmethod
	def ClassId():
		return "adaptorEthPortMcastStats"

	BROADCAST_PACKETS = "BroadcastPackets"
	BROADCAST_PACKETS_DELTA = "BroadcastPacketsDelta"
	BROADCAST_PACKETS_DELTA_AVG = "BroadcastPacketsDeltaAvg"
	BROADCAST_PACKETS_DELTA_MAX = "BroadcastPacketsDeltaMax"
	BROADCAST_PACKETS_DELTA_MIN = "BroadcastPacketsDeltaMin"
	DN = "Dn"
	INTERVALS = "Intervals"
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
	TRAFFIC_DIRECTION = "TrafficDirection"
	UNICAST_PACKETS = "UnicastPackets"
	UNICAST_PACKETS_DELTA = "UnicastPacketsDelta"
	UNICAST_PACKETS_DELTA_AVG = "UnicastPacketsDeltaAvg"
	UNICAST_PACKETS_DELTA_MAX = "UnicastPacketsDeltaMax"
	UNICAST_PACKETS_DELTA_MIN = "UnicastPacketsDeltaMin"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
	CONST_TRAFFIC_DIRECTION_RX = "rx"
	CONST_TRAFFIC_DIRECTION_TX = "tx"
	CONST_TRAFFIC_DIRECTION_UNKNOWN = "unknown"
