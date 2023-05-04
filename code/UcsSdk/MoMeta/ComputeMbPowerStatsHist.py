import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeMbPowerStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeMbPowerStatsHist")

	@staticmethod
	def ClassId():
		return "computeMbPowerStatsHist"

	CONSUMED_POWER = "ConsumedPower"
	CONSUMED_POWER_AVG = "ConsumedPowerAvg"
	CONSUMED_POWER_MAX = "ConsumedPowerMax"
	CONSUMED_POWER_MIN = "ConsumedPowerMin"
	DN = "Dn"
	ID = "Id"
	INPUT_CURRENT = "InputCurrent"
	INPUT_CURRENT_AVG = "InputCurrentAvg"
	INPUT_CURRENT_MAX = "InputCurrentMax"
	INPUT_CURRENT_MIN = "InputCurrentMin"
	INPUT_VOLTAGE = "InputVoltage"
	INPUT_VOLTAGE_AVG = "InputVoltageAvg"
	INPUT_VOLTAGE_MAX = "InputVoltageMax"
	INPUT_VOLTAGE_MIN = "InputVoltageMin"
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
