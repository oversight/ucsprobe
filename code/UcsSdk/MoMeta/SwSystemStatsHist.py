import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwSystemStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwSystemStatsHist")

	@staticmethod
	def ClassId():
		return "swSystemStatsHist"

	DN = "Dn"
	ID = "Id"
	LOAD = "Load"
	LOAD_AVG = "LoadAvg"
	LOAD_MAX = "LoadMax"
	LOAD_MIN = "LoadMin"
	MEM_AVAILABLE = "MemAvailable"
	MEM_AVAILABLE_AVG = "MemAvailableAvg"
	MEM_AVAILABLE_MAX = "MemAvailableMax"
	MEM_AVAILABLE_MIN = "MemAvailableMin"
	MEM_CACHED = "MemCached"
	MEM_CACHED_AVG = "MemCachedAvg"
	MEM_CACHED_MAX = "MemCachedMax"
	MEM_CACHED_MIN = "MemCachedMin"
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
