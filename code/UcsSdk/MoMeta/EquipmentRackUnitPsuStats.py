import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentRackUnitPsuStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentRackUnitPsuStats")

	@staticmethod
	def ClassId():
		return "equipmentRackUnitPsuStats"

	AMBIENT_TEMP = "AmbientTemp"
	AMBIENT_TEMP_AVG = "AmbientTempAvg"
	AMBIENT_TEMP_MAX = "AmbientTempMax"
	AMBIENT_TEMP_MIN = "AmbientTempMin"
	DN = "Dn"
	INPUT_POWER = "InputPower"
	INPUT_POWER_AVG = "InputPowerAvg"
	INPUT_POWER_MAX = "InputPowerMax"
	INPUT_POWER_MIN = "InputPowerMin"
	INPUT_VOLTAGE = "InputVoltage"
	INPUT_VOLTAGE_AVG = "InputVoltageAvg"
	INPUT_VOLTAGE_MAX = "InputVoltageMax"
	INPUT_VOLTAGE_MIN = "InputVoltageMin"
	INTERVALS = "Intervals"
	OUTPUT_CURRENT = "OutputCurrent"
	OUTPUT_CURRENT_AVG = "OutputCurrentAvg"
	OUTPUT_CURRENT_MAX = "OutputCurrentMax"
	OUTPUT_CURRENT_MIN = "OutputCurrentMin"
	OUTPUT_POWER = "OutputPower"
	OUTPUT_POWER_AVG = "OutputPowerAvg"
	OUTPUT_POWER_MAX = "OutputPowerMax"
	OUTPUT_POWER_MIN = "OutputPowerMin"
	OUTPUT_VOLTAGE = "OutputVoltage"
	OUTPUT_VOLTAGE_AVG = "OutputVoltageAvg"
	OUTPUT_VOLTAGE_MAX = "OutputVoltageMax"
	OUTPUT_VOLTAGE_MIN = "OutputVoltageMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"

	CONST_AMBIENT_TEMP_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_INPUT_VOLTAGE_NOT_APPLICABLE = "Not-Applicable"
	CONST_OUTPUT_VOLTAGE_NOT_APPLICABLE = "Not-Applicable"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
