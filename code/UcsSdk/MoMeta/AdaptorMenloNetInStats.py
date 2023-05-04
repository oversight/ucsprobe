import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloNetInStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloNetInStats")

	@staticmethod
	def ClassId():
		return "adaptorMenloNetInStats"

	DN = "Dn"
	DROP_FC_LIF_INVALID = "DropFcLifInvalid"
	DROP_FC_LIF_INVALID_DELTA = "DropFcLifInvalidDelta"
	DROP_FC_LIF_INVALID_DELTA_AVG = "DropFcLifInvalidDeltaAvg"
	DROP_FC_LIF_INVALID_DELTA_MAX = "DropFcLifInvalidDeltaMax"
	DROP_FC_LIF_INVALID_DELTA_MIN = "DropFcLifInvalidDeltaMin"
	DROP_FC_MULTICAST = "DropFcMulticast"
	DROP_FC_MULTICAST_DELTA = "DropFcMulticastDelta"
	DROP_FC_MULTICAST_DELTA_AVG = "DropFcMulticastDeltaAvg"
	DROP_FC_MULTICAST_DELTA_MAX = "DropFcMulticastDeltaMax"
	DROP_FC_MULTICAST_DELTA_MIN = "DropFcMulticastDeltaMin"
	DROP_NULL_PIF = "DropNullPif"
	DROP_NULL_PIF_DELTA = "DropNullPifDelta"
	DROP_NULL_PIF_DELTA_AVG = "DropNullPifDeltaAvg"
	DROP_NULL_PIF_DELTA_MAX = "DropNullPifDeltaMax"
	DROP_NULL_PIF_DELTA_MIN = "DropNullPifDeltaMin"
	FWD_LOOKUP_NO_HIT = "FwdLookupNoHit"
	FWD_LOOKUP_NO_HIT_DELTA = "FwdLookupNoHitDelta"
	FWD_LOOKUP_NO_HIT_DELTA_AVG = "FwdLookupNoHitDeltaAvg"
	FWD_LOOKUP_NO_HIT_DELTA_MAX = "FwdLookupNoHitDeltaMax"
	FWD_LOOKUP_NO_HIT_DELTA_MIN = "FwdLookupNoHitDeltaMin"
	INTERVALS = "Intervals"
	MENLO_NET_INDEX = "MenloNetIndex"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"

	CONST_MENLO_NET_INDEX_0 = "0"
	CONST_MENLO_NET_INDEX_0_A = "0_A"
	CONST_MENLO_NET_INDEX_0_B = "0_B"
	CONST_MENLO_NET_INDEX_1 = "1"
	CONST_MENLO_NET_INDEX_1_A = "1_A"
	CONST_MENLO_NET_INDEX_1_B = "1_B"
	CONST_MENLO_NET_INDEX_UNKNOWN = "unknown"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
