import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeIOHubEnvStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeIOHubEnvStats")

	@staticmethod
	def ClassId():
		return "computeIOHubEnvStats"

	DN = "Dn"
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
	CONST_TEMPERATURE_NOT_APPLICABLE = "not-applicable"
	CONST_TEMPERATURE_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_TEMPERATURE_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_TEMPERATURE_MIN_NOT_APPLICABLE = "not-applicable"
