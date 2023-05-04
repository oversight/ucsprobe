import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentFexPsuInputStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentFexPsuInputStats")

	@staticmethod
	def ClassId():
		return "equipmentFexPsuInputStats"

	CURRENT = "Current"
	CURRENT_AVG = "CurrentAvg"
	CURRENT_MAX = "CurrentMax"
	CURRENT_MIN = "CurrentMin"
	DN = "Dn"
	INPUT_STATUS = "InputStatus"
	INTERVALS = "Intervals"
	POWER = "Power"
	POWER_AVG = "PowerAvg"
	POWER_MAX = "PowerMax"
	POWER_MIN = "PowerMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"
	VOLTAGE = "Voltage"
	VOLTAGE_AVG = "VoltageAvg"
	VOLTAGE_MAX = "VoltageMax"
	VOLTAGE_MIN = "VoltageMin"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
