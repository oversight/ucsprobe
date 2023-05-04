import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProcessorEnvStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ProcessorEnvStats")

	@staticmethod
	def ClassId():
		return "processorEnvStats"

	DN = "Dn"
	INPUT_CURRENT = "InputCurrent"
	INPUT_CURRENT_AVG = "InputCurrentAvg"
	INPUT_CURRENT_MAX = "InputCurrentMax"
	INPUT_CURRENT_MIN = "InputCurrentMin"
	INTERVALS = "Intervals"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	TEMPERATURE = "Temperature"
	TEMPERATURE_AVG = "TemperatureAvg"
	TEMPERATURE_MAX = "TemperatureMax"
	TEMPERATURE_MIN = "TemperatureMin"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
