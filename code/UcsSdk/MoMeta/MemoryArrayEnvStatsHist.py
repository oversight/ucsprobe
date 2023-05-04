import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MemoryArrayEnvStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MemoryArrayEnvStatsHist")

	@staticmethod
	def ClassId():
		return "memoryArrayEnvStatsHist"

	DN = "Dn"
	ID = "Id"
	INPUT_CURRENT = "InputCurrent"
	INPUT_CURRENT_AVG = "InputCurrentAvg"
	INPUT_CURRENT_MAX = "InputCurrentMax"
	INPUT_CURRENT_MIN = "InputCurrentMin"
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
