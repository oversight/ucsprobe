import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentRackUnitFanStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentRackUnitFanStats")

	@staticmethod
	def ClassId():
		return "equipmentRackUnitFanStats"

	DN = "Dn"
	INTERVALS = "Intervals"
	RN = "Rn"
	SPEED = "Speed"
	SPEED_AVG = "SpeedAvg"
	SPEED_MAX = "SpeedMax"
	SPEED_MIN = "SpeedMin"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
