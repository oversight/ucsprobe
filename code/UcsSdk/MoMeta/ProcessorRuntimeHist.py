import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProcessorRuntimeHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ProcessorRuntimeHist")

	@staticmethod
	def ClassId():
		return "processorRuntimeHist"

	DN = "Dn"
	ID = "Id"
	LOAD = "Load"
	LOAD_AVG = "LoadAvg"
	LOAD_MAX = "LoadMax"
	LOAD_MIN = "LoadMin"
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
