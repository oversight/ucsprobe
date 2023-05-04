import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPsuInputStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPsuInputStatsHist")

	@staticmethod
	def ClassId():
		return "equipmentPsuInputStatsHist"

	CURRENT = "Current"
	CURRENT_AVG = "CurrentAvg"
	CURRENT_MAX = "CurrentMax"
	CURRENT_MIN = "CurrentMin"
	DN = "Dn"
	ID = "Id"
	MOST_RECENT = "MostRecent"
	POWER = "Power"
	POWER_AVG = "PowerAvg"
	POWER_MAX = "PowerMax"
	POWER_MIN = "PowerMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	VOLTAGE = "Voltage"
	VOLTAGE_AVG = "VoltageAvg"
	VOLTAGE_MAX = "VoltageMax"
	VOLTAGE_MIN = "VoltageMin"

	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
