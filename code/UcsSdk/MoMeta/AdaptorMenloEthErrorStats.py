import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloEthErrorStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloEthErrorStats")

	@staticmethod
	def ClassId():
		return "adaptorMenloEthErrorStats"

	CORRECTABLE_ERRORS = "CorrectableErrors"
	CORRECTABLE_ERRORS_DELTA = "CorrectableErrorsDelta"
	CORRECTABLE_ERRORS_DELTA_AVG = "CorrectableErrorsDeltaAvg"
	CORRECTABLE_ERRORS_DELTA_MAX = "CorrectableErrorsDeltaMax"
	CORRECTABLE_ERRORS_DELTA_MIN = "CorrectableErrorsDeltaMin"
	DN = "Dn"
	DROP_ACL = "DropAcl"
	DROP_ACL_DELTA = "DropAclDelta"
	DROP_ACL_DELTA_AVG = "DropAclDeltaAvg"
	DROP_ACL_DELTA_MAX = "DropAclDeltaMax"
	DROP_ACL_DELTA_MIN = "DropAclDeltaMin"
	INTERVALS = "Intervals"
	MENLO_ETH_INDEX = "MenloEthIndex"
	POP_ERRORS = "PopErrors"
	POP_ERRORS_DELTA = "PopErrorsDelta"
	POP_ERRORS_DELTA_AVG = "PopErrorsDeltaAvg"
	POP_ERRORS_DELTA_MAX = "PopErrorsDeltaMax"
	POP_ERRORS_DELTA_MIN = "PopErrorsDeltaMin"
	PUSH_ERRORS = "PushErrors"
	PUSH_ERRORS_DELTA = "PushErrorsDelta"
	PUSH_ERRORS_DELTA_AVG = "PushErrorsDeltaAvg"
	PUSH_ERRORS_DELTA_MAX = "PushErrorsDeltaMax"
	PUSH_ERRORS_DELTA_MIN = "PushErrorsDeltaMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UNCORRECTABLE_ERRORS = "UncorrectableErrors"
	UNCORRECTABLE_ERRORS_DELTA = "UncorrectableErrorsDelta"
	UNCORRECTABLE_ERRORS_DELTA_AVG = "UncorrectableErrorsDeltaAvg"
	UNCORRECTABLE_ERRORS_DELTA_MAX = "UncorrectableErrorsDeltaMax"
	UNCORRECTABLE_ERRORS_DELTA_MIN = "UncorrectableErrorsDeltaMin"
	UPDATE = "Update"

	CONST_MENLO_ETH_INDEX_0 = "0"
	CONST_MENLO_ETH_INDEX_0_A = "0_A"
	CONST_MENLO_ETH_INDEX_0_B = "0_B"
	CONST_MENLO_ETH_INDEX_1 = "1"
	CONST_MENLO_ETH_INDEX_1_A = "1_A"
	CONST_MENLO_ETH_INDEX_1_B = "1_B"
	CONST_MENLO_ETH_INDEX_UNKNOWN = "unknown"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
