import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentFexPowerSummaryHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentFexPowerSummaryHist")

	@staticmethod
	def ClassId():
		return "equipmentFexPowerSummaryHist"

	_MODULE_POWER = "ModulePower"
	_MODULE_POWER_AVG = "ModulePowerAvg"
	_MODULE_POWER_MAX = "ModulePowerMax"
	_MODULE_POWER_MIN = "ModulePowerMin"
	AVAILABLE_POWER = "AvailablePower"
	AVAILABLE_POWER_AVG = "AvailablePowerAvg"
	AVAILABLE_POWER_MAX = "AvailablePowerMax"
	AVAILABLE_POWER_MIN = "AvailablePowerMin"
	DN = "Dn"
	ID = "Id"
	MOST_RECENT = "MostRecent"
	RESERVED_POWER = "ReservedPower"
	RESERVED_POWER_AVG = "ReservedPowerAvg"
	RESERVED_POWER_MAX = "ReservedPowerMax"
	RESERVED_POWER_MIN = "ReservedPowerMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TOTAL_POWER = "TotalPower"
	TOTAL_POWER_AVG = "TotalPowerAvg"
	TOTAL_POWER_MAX = "TotalPowerMax"
	TOTAL_POWER_MIN = "TotalPowerMin"

	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
