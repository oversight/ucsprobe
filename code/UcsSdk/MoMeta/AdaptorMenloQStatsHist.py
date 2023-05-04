import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloQStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloQStatsHist")

	@staticmethod
	def ClassId():
		return "adaptorMenloQStatsHist"

	DN = "Dn"
	DROP_OVERRUN_N0 = "DropOverrunN0"
	DROP_OVERRUN_N0_DELTA = "DropOverrunN0Delta"
	DROP_OVERRUN_N0_DELTA_AVG = "DropOverrunN0DeltaAvg"
	DROP_OVERRUN_N0_DELTA_MAX = "DropOverrunN0DeltaMax"
	DROP_OVERRUN_N0_DELTA_MIN = "DropOverrunN0DeltaMin"
	DROP_OVERRUN_N1 = "DropOverrunN1"
	DROP_OVERRUN_N1_DELTA = "DropOverrunN1Delta"
	DROP_OVERRUN_N1_DELTA_AVG = "DropOverrunN1DeltaAvg"
	DROP_OVERRUN_N1_DELTA_MAX = "DropOverrunN1DeltaMax"
	DROP_OVERRUN_N1_DELTA_MIN = "DropOverrunN1DeltaMin"
	ID = "Id"
	MOST_RECENT = "MostRecent"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TRUNCATE_OVERRUN_N0 = "TruncateOverrunN0"
	TRUNCATE_OVERRUN_N0_DELTA = "TruncateOverrunN0Delta"
	TRUNCATE_OVERRUN_N0_DELTA_AVG = "TruncateOverrunN0DeltaAvg"
	TRUNCATE_OVERRUN_N0_DELTA_MAX = "TruncateOverrunN0DeltaMax"
	TRUNCATE_OVERRUN_N0_DELTA_MIN = "TruncateOverrunN0DeltaMin"
	TRUNCATE_OVERRUN_N1 = "TruncateOverrunN1"
	TRUNCATE_OVERRUN_N1_DELTA = "TruncateOverrunN1Delta"
	TRUNCATE_OVERRUN_N1_DELTA_AVG = "TruncateOverrunN1DeltaAvg"
	TRUNCATE_OVERRUN_N1_DELTA_MAX = "TruncateOverrunN1DeltaMax"
	TRUNCATE_OVERRUN_N1_DELTA_MIN = "TruncateOverrunN1DeltaMin"

	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
