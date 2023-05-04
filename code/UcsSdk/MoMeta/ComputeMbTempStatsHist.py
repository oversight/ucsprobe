import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeMbTempStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeMbTempStatsHist")

	@staticmethod
	def ClassId():
		return "computeMbTempStatsHist"

	DN = "Dn"
	FM_TEMP_SEN_IO = "FmTempSenIo"
	FM_TEMP_SEN_IO_AVG = "FmTempSenIoAvg"
	FM_TEMP_SEN_IO_MAX = "FmTempSenIoMax"
	FM_TEMP_SEN_IO_MIN = "FmTempSenIoMin"
	FM_TEMP_SEN_REAR = "FmTempSenRear"
	FM_TEMP_SEN_REAR_AVG = "FmTempSenRearAvg"
	FM_TEMP_SEN_REAR_L = "FmTempSenRearL"
	FM_TEMP_SEN_REAR_LAVG = "FmTempSenRearLAvg"
	FM_TEMP_SEN_REAR_LMAX = "FmTempSenRearLMax"
	FM_TEMP_SEN_REAR_LMIN = "FmTempSenRearLMin"
	FM_TEMP_SEN_REAR_MAX = "FmTempSenRearMax"
	FM_TEMP_SEN_REAR_MIN = "FmTempSenRearMin"
	FM_TEMP_SEN_REAR_R = "FmTempSenRearR"
	FM_TEMP_SEN_REAR_RAVG = "FmTempSenRearRAvg"
	FM_TEMP_SEN_REAR_RMAX = "FmTempSenRearRMax"
	FM_TEMP_SEN_REAR_RMIN = "FmTempSenRearRMin"
	ID = "Id"
	MOST_RECENT = "MostRecent"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"

	CONST_FM_TEMP_SEN_IO_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_IO_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_IO_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_IO_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_L_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_LAVG_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_LMAX_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_LMIN_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_R_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_RAVG_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_RMAX_NOT_APPLICABLE = "not-applicable"
	CONST_FM_TEMP_SEN_REAR_RMIN_NOT_APPLICABLE = "not-applicable"
	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
