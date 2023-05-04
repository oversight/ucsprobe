import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloNetEgStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloNetEgStats")

	@staticmethod
	def ClassId():
		return "adaptorMenloNetEgStats"

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
	INTERVALS = "Intervals"
	LEARN_REQ_DROP = "LearnReqDrop"
	LEARN_REQ_DROP_DELTA = "LearnReqDropDelta"
	LEARN_REQ_DROP_DELTA_AVG = "LearnReqDropDeltaAvg"
	LEARN_REQ_DROP_DELTA_MAX = "LearnReqDropDeltaMax"
	LEARN_REQ_DROP_DELTA_MIN = "LearnReqDropDeltaMin"
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
