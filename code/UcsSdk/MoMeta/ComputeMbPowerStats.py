import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeMbPowerStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeMbPowerStats")

	@staticmethod
	def ClassId():
		return "computeMbPowerStats"

	CONSUMED_POWER = "ConsumedPower"
	CONSUMED_POWER_AVG = "ConsumedPowerAvg"
	CONSUMED_POWER_MAX = "ConsumedPowerMax"
	CONSUMED_POWER_MIN = "ConsumedPowerMin"
	DN = "Dn"
	INPUT_CURRENT = "InputCurrent"
	INPUT_CURRENT_AVG = "InputCurrentAvg"
	INPUT_CURRENT_MAX = "InputCurrentMax"
	INPUT_CURRENT_MIN = "InputCurrentMin"
	INPUT_VOLTAGE = "InputVoltage"
	INPUT_VOLTAGE_AVG = "InputVoltageAvg"
	INPUT_VOLTAGE_MAX = "InputVoltageMax"
	INPUT_VOLTAGE_MIN = "InputVoltageMin"
	INTERVALS = "Intervals"
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
