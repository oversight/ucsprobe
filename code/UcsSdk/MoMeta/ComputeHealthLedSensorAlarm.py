import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeHealthLedSensorAlarm(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeHealthLedSensorAlarm")

	@staticmethod
	def ClassId():
		return "computeHealthLedSensorAlarm"

	ALARM_DESC = "AlarmDesc"
	ALARM_SEVERITY = "AlarmSeverity"
	DN = "Dn"
	RN = "Rn"
	SENSOR_ID = "SensorId"
	SENSOR_NAME = "SensorName"
	STATUS = "Status"

	CONST_ALARM_SEVERITY_MINOR = "minor"
	CONST_ALARM_SEVERITY_SEVERE = "severe"
