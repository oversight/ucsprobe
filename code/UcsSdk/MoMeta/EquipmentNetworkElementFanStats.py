import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentNetworkElementFanStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentNetworkElementFanStats")

	@staticmethod
	def ClassId():
		return "equipmentNetworkElementFanStats"

	AIRFLOW_DIRECTION = "AirflowDirection"
	DN = "Dn"
	DRIVE_PERCENTAGE = "DrivePercentage"
	DRIVE_PERCENTAGE_AVG = "DrivePercentageAvg"
	DRIVE_PERCENTAGE_MAX = "DrivePercentageMax"
	DRIVE_PERCENTAGE_MIN = "DrivePercentageMin"
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

	CONST_AIRFLOW_DIRECTION_BACK_TO_FRONT = "BackToFront"
	CONST_AIRFLOW_DIRECTION_FRONT_TO_BACK = "FrontToBack"
	CONST_AIRFLOW_DIRECTION_UNKNOWN = "unknown"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
