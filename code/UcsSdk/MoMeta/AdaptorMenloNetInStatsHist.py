import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloNetInStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloNetInStatsHist")

	@staticmethod
	def ClassId():
		return "adaptorMenloNetInStatsHist"

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
	ID = "Id"
	MOST_RECENT = "MostRecent"
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
