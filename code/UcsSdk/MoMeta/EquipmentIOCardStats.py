import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentIOCardStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentIOCardStats")

	@staticmethod
	def ClassId():
		return "equipmentIOCardStats"

	AMBIENT_TEMP = "AmbientTemp"
	AMBIENT_TEMP_AVG = "AmbientTempAvg"
	AMBIENT_TEMP_MAX = "AmbientTempMax"
	AMBIENT_TEMP_MIN = "AmbientTempMin"
	DN = "Dn"
	INTERVALS = "Intervals"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	TEMP = "Temp"
	TEMP_AVG = "TempAvg"
	TEMP_MAX = "TempMax"
	TEMP_MIN = "TempMin"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"

	CONST_AMBIENT_TEMP_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
	CONST_TEMP_NOT_APPLICABLE = "not-applicable"
	CONST_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
