import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MemoryRuntimeHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MemoryRuntimeHist")

	@staticmethod
	def ClassId():
		return "memoryRuntimeHist"

	AVAILABLE = "Available"
	AVAILABLE_AVG = "AvailableAvg"
	AVAILABLE_MAX = "AvailableMax"
	AVAILABLE_MIN = "AvailableMin"
	CACHED = "Cached"
	CACHED_AVG = "CachedAvg"
	CACHED_MAX = "CachedMax"
	CACHED_MIN = "CachedMin"
	DN = "Dn"
	ID = "Id"
	MOST_RECENT = "MostRecent"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TOTAL = "Total"
	TOTAL_AVG = "TotalAvg"
	TOTAL_MAX = "TotalMax"
	TOTAL_MIN = "TotalMin"

	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
