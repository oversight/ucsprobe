import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloMcpuErrorStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloMcpuErrorStatsHist")

	@staticmethod
	def ClassId():
		return "adaptorMenloMcpuErrorStatsHist"

	CORRECTABLE_ERRORS = "CorrectableErrors"
	CORRECTABLE_ERRORS_DELTA = "CorrectableErrorsDelta"
	CORRECTABLE_ERRORS_DELTA_AVG = "CorrectableErrorsDeltaAvg"
	CORRECTABLE_ERRORS_DELTA_MAX = "CorrectableErrorsDeltaMax"
	CORRECTABLE_ERRORS_DELTA_MIN = "CorrectableErrorsDeltaMin"
	DN = "Dn"
	ID = "Id"
	MOST_RECENT = "MostRecent"
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

	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
