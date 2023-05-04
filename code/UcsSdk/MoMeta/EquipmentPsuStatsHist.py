import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPsuStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPsuStatsHist")

	@staticmethod
	def ClassId():
		return "equipmentPsuStatsHist"

	AMBIENT_TEMP = "AmbientTemp"
	AMBIENT_TEMP_AVG = "AmbientTempAvg"
	AMBIENT_TEMP_MAX = "AmbientTempMax"
	AMBIENT_TEMP_MIN = "AmbientTempMin"
	DN = "Dn"
	ID = "Id"
	INPUT210V = "Input210v"
	INPUT210V_AVG = "Input210vAvg"
	INPUT210V_MAX = "Input210vMax"
	INPUT210V_MIN = "Input210vMin"
	MOST_RECENT = "MostRecent"
	OUTPUT12V = "Output12v"
	OUTPUT12V_AVG = "Output12vAvg"
	OUTPUT12V_MAX = "Output12vMax"
	OUTPUT12V_MIN = "Output12vMin"
	OUTPUT3V3 = "Output3v3"
	OUTPUT3V3_AVG = "Output3v3Avg"
	OUTPUT3V3_MAX = "Output3v3Max"
	OUTPUT3V3_MIN = "Output3v3Min"
	OUTPUT_CURRENT = "OutputCurrent"
	OUTPUT_CURRENT_AVG = "OutputCurrentAvg"
	OUTPUT_CURRENT_MAX = "OutputCurrentMax"
	OUTPUT_CURRENT_MIN = "OutputCurrentMin"
	OUTPUT_POWER = "OutputPower"
	OUTPUT_POWER_AVG = "OutputPowerAvg"
	OUTPUT_POWER_MAX = "OutputPowerMax"
	OUTPUT_POWER_MIN = "OutputPowerMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"

	CONST_AMBIENT_TEMP_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
