import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEthPortStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEthPortStats")

	@staticmethod
	def ClassId():
		return "adaptorEthPortStats"

	DN = "Dn"
	GOOD_PACKETS = "GoodPackets"
	GOOD_PACKETS_DELTA = "GoodPacketsDelta"
	GOOD_PACKETS_DELTA_AVG = "GoodPacketsDeltaAvg"
	GOOD_PACKETS_DELTA_MAX = "GoodPacketsDeltaMax"
	GOOD_PACKETS_DELTA_MIN = "GoodPacketsDeltaMin"
	INTERVALS = "Intervals"
	PAUSE_PACKETS = "PausePackets"
	PAUSE_PACKETS_DELTA = "PausePacketsDelta"
	PAUSE_PACKETS_DELTA_AVG = "PausePacketsDeltaAvg"
	PAUSE_PACKETS_DELTA_MAX = "PausePacketsDeltaMax"
	PAUSE_PACKETS_DELTA_MIN = "PausePacketsDeltaMin"
	PER_PRIORITY_PAUSE_PACKETS = "PerPriorityPausePackets"
	PER_PRIORITY_PAUSE_PACKETS_DELTA = "PerPriorityPausePacketsDelta"
	PER_PRIORITY_PAUSE_PACKETS_DELTA_AVG = "PerPriorityPausePacketsDeltaAvg"
	PER_PRIORITY_PAUSE_PACKETS_DELTA_MAX = "PerPriorityPausePacketsDeltaMax"
	PER_PRIORITY_PAUSE_PACKETS_DELTA_MIN = "PerPriorityPausePacketsDeltaMin"
	PPP_PACKETS = "PppPackets"
	PPP_PACKETS_DELTA = "PppPacketsDelta"
	PPP_PACKETS_DELTA_AVG = "PppPacketsDeltaAvg"
	PPP_PACKETS_DELTA_MAX = "PppPacketsDeltaMax"
	PPP_PACKETS_DELTA_MIN = "PppPacketsDeltaMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TOTAL_PACKETS = "TotalPackets"
	TOTAL_PACKETS_DELTA = "TotalPacketsDelta"
	TOTAL_PACKETS_DELTA_AVG = "TotalPacketsDeltaAvg"
	TOTAL_PACKETS_DELTA_MAX = "TotalPacketsDeltaMax"
	TOTAL_PACKETS_DELTA_MIN = "TotalPacketsDeltaMin"
	TRAFFIC_DIRECTION = "TrafficDirection"
	UPDATE = "Update"
	VLAN_PACKETS = "VlanPackets"
	VLAN_PACKETS_DELTA = "VlanPacketsDelta"
	VLAN_PACKETS_DELTA_AVG = "VlanPacketsDeltaAvg"
	VLAN_PACKETS_DELTA_MAX = "VlanPacketsDeltaMax"
	VLAN_PACKETS_DELTA_MIN = "VlanPacketsDeltaMin"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
	CONST_TRAFFIC_DIRECTION_RX = "rx"
	CONST_TRAFFIC_DIRECTION_TX = "tx"
	CONST_TRAFFIC_DIRECTION_UNKNOWN = "unknown"
