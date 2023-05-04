import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloQErrorStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloQErrorStats")

	@staticmethod
	def ClassId():
		return "adaptorMenloQErrorStats"

	CORRECTABLE_ERRORS = "CorrectableErrors"
	CORRECTABLE_ERRORS_DELTA = "CorrectableErrorsDelta"
	CORRECTABLE_ERRORS_DELTA_AVG = "CorrectableErrorsDeltaAvg"
	CORRECTABLE_ERRORS_DELTA_MAX = "CorrectableErrorsDeltaMax"
	CORRECTABLE_ERRORS_DELTA_MIN = "CorrectableErrorsDeltaMin"
	DN = "Dn"
	INTERVALS = "Intervals"
	MENLO_QUEUE_COMPONENT = "MenloQueueComponent"
	MENLO_QUEUE_INDEX = "MenloQueueIndex"
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

	CONST_MENLO_QUEUE_COMPONENT_N = "N"
	CONST_MENLO_QUEUE_COMPONENT_CPU = "cpu"
	CONST_MENLO_QUEUE_COMPONENT_ETH = "eth"
	CONST_MENLO_QUEUE_COMPONENT_FC = "fc"
	CONST_MENLO_QUEUE_COMPONENT_UNKNOWN = "unknown"
	CONST_MENLO_QUEUE_INDEX_0 = "0"
	CONST_MENLO_QUEUE_INDEX_0_A = "0_A"
	CONST_MENLO_QUEUE_INDEX_0_B = "0_B"
	CONST_MENLO_QUEUE_INDEX_1 = "1"
	CONST_MENLO_QUEUE_INDEX_1_A = "1_A"
	CONST_MENLO_QUEUE_INDEX_1_B = "1_B"
	CONST_MENLO_QUEUE_INDEX_UNKNOWN = "unknown"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
