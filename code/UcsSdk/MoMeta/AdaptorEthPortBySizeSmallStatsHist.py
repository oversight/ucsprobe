import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEthPortBySizeSmallStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEthPortBySizeSmallStatsHist")

	@staticmethod
	def ClassId():
		return "adaptorEthPortBySizeSmallStatsHist"

	DN = "Dn"
	EQUALS64 = "Equals64"
	EQUALS64_DELTA = "Equals64Delta"
	EQUALS64_DELTA_AVG = "Equals64DeltaAvg"
	EQUALS64_DELTA_MAX = "Equals64DeltaMax"
	EQUALS64_DELTA_MIN = "Equals64DeltaMin"
	ID = "Id"
	LESS_THAN1024 = "LessThan1024"
	LESS_THAN1024_DELTA = "LessThan1024Delta"
	LESS_THAN1024_DELTA_AVG = "LessThan1024DeltaAvg"
	LESS_THAN1024_DELTA_MAX = "LessThan1024DeltaMax"
	LESS_THAN1024_DELTA_MIN = "LessThan1024DeltaMin"
	LESS_THAN128 = "LessThan128"
	LESS_THAN128_DELTA = "LessThan128Delta"
	LESS_THAN128_DELTA_AVG = "LessThan128DeltaAvg"
	LESS_THAN128_DELTA_MAX = "LessThan128DeltaMax"
	LESS_THAN128_DELTA_MIN = "LessThan128DeltaMin"
	LESS_THAN256 = "LessThan256"
	LESS_THAN256_DELTA = "LessThan256Delta"
	LESS_THAN256_DELTA_AVG = "LessThan256DeltaAvg"
	LESS_THAN256_DELTA_MAX = "LessThan256DeltaMax"
	LESS_THAN256_DELTA_MIN = "LessThan256DeltaMin"
	LESS_THAN512 = "LessThan512"
	LESS_THAN512_DELTA = "LessThan512Delta"
	LESS_THAN512_DELTA_AVG = "LessThan512DeltaAvg"
	LESS_THAN512_DELTA_MAX = "LessThan512DeltaMax"
	LESS_THAN512_DELTA_MIN = "LessThan512DeltaMin"
	LESS_THAN64 = "LessThan64"
	LESS_THAN64_DELTA = "LessThan64Delta"
	LESS_THAN64_DELTA_AVG = "LessThan64DeltaAvg"
	LESS_THAN64_DELTA_MAX = "LessThan64DeltaMax"
	LESS_THAN64_DELTA_MIN = "LessThan64DeltaMin"
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
