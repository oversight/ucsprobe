import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeRackUnitMbTempStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeRackUnitMbTempStats")

	@staticmethod
	def ClassId():
		return "computeRackUnitMbTempStats"

	AMBIENT_TEMP = "AmbientTemp"
	AMBIENT_TEMP_AVG = "AmbientTempAvg"
	AMBIENT_TEMP_MAX = "AmbientTempMax"
	AMBIENT_TEMP_MIN = "AmbientTempMin"
	DN = "Dn"
	FRONT_TEMP = "FrontTemp"
	FRONT_TEMP_AVG = "FrontTempAvg"
	FRONT_TEMP_MAX = "FrontTempMax"
	FRONT_TEMP_MIN = "FrontTempMin"
	INTERVALS = "Intervals"
	IOH1_TEMP = "Ioh1Temp"
	IOH1_TEMP_AVG = "Ioh1TempAvg"
	IOH1_TEMP_MAX = "Ioh1TempMax"
	IOH1_TEMP_MIN = "Ioh1TempMin"
	IOH2_TEMP = "Ioh2Temp"
	IOH2_TEMP_AVG = "Ioh2TempAvg"
	IOH2_TEMP_MAX = "Ioh2TempMax"
	IOH2_TEMP_MIN = "Ioh2TempMin"
	REAR_TEMP = "RearTemp"
	REAR_TEMP_AVG = "RearTempAvg"
	REAR_TEMP_MAX = "RearTempMax"
	REAR_TEMP_MIN = "RearTempMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"

	CONST_AMBIENT_TEMP_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_AMBIENT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_FRONT_TEMP_NOT_APPLICABLE = "not-applicable"
	CONST_FRONT_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_FRONT_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_FRONT_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_IOH1_TEMP_NOT_APPLICABLE = "not-applicable"
	CONST_IOH1_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_IOH1_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_IOH1_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_IOH2_TEMP_NOT_APPLICABLE = "not-applicable"
	CONST_IOH2_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_IOH2_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_IOH2_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_REAR_TEMP_NOT_APPLICABLE = "not-applicable"
	CONST_REAR_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_REAR_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_REAR_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
