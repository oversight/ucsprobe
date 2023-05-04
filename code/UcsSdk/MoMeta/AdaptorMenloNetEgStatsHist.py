import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloNetEgStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloNetEgStatsHist")

	@staticmethod
	def ClassId():
		return "adaptorMenloNetEgStatsHist"

	DN = "Dn"
	DROP_CMD = "DropCmd"
	DROP_CMD_DELTA = "DropCmdDelta"
	DROP_CMD_DELTA_AVG = "DropCmdDeltaAvg"
	DROP_CMD_DELTA_MAX = "DropCmdDeltaMax"
	DROP_CMD_DELTA_MIN = "DropCmdDeltaMin"
	DROP_LIF_CFG_INVALID = "DropLifCfgInvalid"
	DROP_LIF_CFG_INVALID_DELTA = "DropLifCfgInvalidDelta"
	DROP_LIF_CFG_INVALID_DELTA_AVG = "DropLifCfgInvalidDeltaAvg"
	DROP_LIF_CFG_INVALID_DELTA_MAX = "DropLifCfgInvalidDeltaMax"
	DROP_LIF_CFG_INVALID_DELTA_MIN = "DropLifCfgInvalidDeltaMin"
	DROP_LIF_MAP_NO_HIT = "DropLifMapNoHit"
	DROP_LIF_MAP_NO_HIT_DELTA = "DropLifMapNoHitDelta"
	DROP_LIF_MAP_NO_HIT_DELTA_AVG = "DropLifMapNoHitDeltaAvg"
	DROP_LIF_MAP_NO_HIT_DELTA_MAX = "DropLifMapNoHitDeltaMax"
	DROP_LIF_MAP_NO_HIT_DELTA_MIN = "DropLifMapNoHitDeltaMin"
	DROP_SRC_BIND = "DropSrcBind"
	DROP_SRC_BIND_DELTA = "DropSrcBindDelta"
	DROP_SRC_BIND_DELTA_AVG = "DropSrcBindDeltaAvg"
	DROP_SRC_BIND_DELTA_MAX = "DropSrcBindDeltaMax"
	DROP_SRC_BIND_DELTA_MIN = "DropSrcBindDeltaMin"
	ID = "Id"
	LEARN_REQ_DROP = "LearnReqDrop"
	LEARN_REQ_DROP_DELTA = "LearnReqDropDelta"
	LEARN_REQ_DROP_DELTA_AVG = "LearnReqDropDeltaAvg"
	LEARN_REQ_DROP_DELTA_MAX = "LearnReqDropDeltaMax"
	LEARN_REQ_DROP_DELTA_MIN = "LearnReqDropDeltaMin"
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
