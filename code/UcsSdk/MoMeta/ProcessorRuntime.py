import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProcessorRuntime(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ProcessorRuntime")

	@staticmethod
	def ClassId():
		return "processorRuntime"

	DN = "Dn"
	INTERVALS = "Intervals"
	LOAD = "Load"
	LOAD_AVG = "LoadAvg"
	LOAD_MAX = "LoadMax"
	LOAD_MIN = "LoadMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"
	UPTIME = "Uptime"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
