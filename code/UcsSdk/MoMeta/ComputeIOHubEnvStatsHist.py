import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeIOHubEnvStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeIOHubEnvStatsHist")

	@staticmethod
	def ClassId():
		return "computeIOHubEnvStatsHist"

	DN = "Dn"
	ID = "Id"
	MOST_RECENT = "MostRecent"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	TEMPERATURE = "Temperature"
	TEMPERATURE_AVG = "TemperatureAvg"
	TEMPERATURE_MAX = "TemperatureMax"
	TEMPERATURE_MIN = "TemperatureMin"
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
	CONST_TEMPERATURE_NOT_APPLICABLE = "not-applicable"
	CONST_TEMPERATURE_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_TEMPERATURE_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_TEMPERATURE_MIN_NOT_APPLICABLE = "not-applicable"
