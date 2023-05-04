import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentNetworkElementFanStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentNetworkElementFanStatsHist")

	@staticmethod
	def ClassId():
		return "equipmentNetworkElementFanStatsHist"

	DN = "Dn"
	DRIVE_PERCENTAGE = "DrivePercentage"
	DRIVE_PERCENTAGE_AVG = "DrivePercentageAvg"
	DRIVE_PERCENTAGE_MAX = "DrivePercentageMax"
	DRIVE_PERCENTAGE_MIN = "DrivePercentageMin"
	ID = "Id"
	MOST_RECENT = "MostRecent"
	RN = "Rn"
	SPEED = "Speed"
	SPEED_AVG = "SpeedAvg"
	SPEED_MAX = "SpeedMax"
	SPEED_MIN = "SpeedMin"
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
