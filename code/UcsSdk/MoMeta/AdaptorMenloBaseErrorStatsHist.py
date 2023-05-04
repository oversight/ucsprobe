import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloBaseErrorStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloBaseErrorStatsHist")

	@staticmethod
	def ClassId():
		return "adaptorMenloBaseErrorStatsHist"

	CORRECTABLE_ERRORS = "CorrectableErrors"
	CORRECTABLE_ERRORS_DELTA = "CorrectableErrorsDelta"
	CORRECTABLE_ERRORS_DELTA_AVG = "CorrectableErrorsDeltaAvg"
	CORRECTABLE_ERRORS_DELTA_MAX = "CorrectableErrorsDeltaMax"
	CORRECTABLE_ERRORS_DELTA_MIN = "CorrectableErrorsDeltaMin"
	DN = "Dn"
	ID = "Id"
	MOST_RECENT = "MostRecent"
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
