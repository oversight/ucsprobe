import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentChassisStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentChassisStats")

	@staticmethod
	def ClassId():
		return "equipmentChassisStats"

	DN = "Dn"
	INPUT_POWER = "InputPower"
	INPUT_POWER_AVG = "InputPowerAvg"
	INPUT_POWER_MAX = "InputPowerMax"
	INPUT_POWER_MIN = "InputPowerMin"
	INTERVALS = "Intervals"
	OUTPUT_POWER = "OutputPower"
	OUTPUT_POWER_AVG = "OutputPowerAvg"
	OUTPUT_POWER_MAX = "OutputPowerMax"
	OUTPUT_POWER_MIN = "OutputPowerMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
