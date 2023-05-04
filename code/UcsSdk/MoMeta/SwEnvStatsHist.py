import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwEnvStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwEnvStatsHist")

	@staticmethod
	def ClassId():
		return "swEnvStatsHist"

	DN = "Dn"
	FAN_CTRLR_INLET1 = "FanCtrlrInlet1"
	FAN_CTRLR_INLET1_AVG = "FanCtrlrInlet1Avg"
	FAN_CTRLR_INLET1_MAX = "FanCtrlrInlet1Max"
	FAN_CTRLR_INLET1_MIN = "FanCtrlrInlet1Min"
	FAN_CTRLR_INLET2 = "FanCtrlrInlet2"
	FAN_CTRLR_INLET2_AVG = "FanCtrlrInlet2Avg"
	FAN_CTRLR_INLET2_MAX = "FanCtrlrInlet2Max"
	FAN_CTRLR_INLET2_MIN = "FanCtrlrInlet2Min"
	FAN_CTRLR_INLET3 = "FanCtrlrInlet3"
	FAN_CTRLR_INLET3_AVG = "FanCtrlrInlet3Avg"
	FAN_CTRLR_INLET3_MAX = "FanCtrlrInlet3Max"
	FAN_CTRLR_INLET3_MIN = "FanCtrlrInlet3Min"
	FAN_CTRLR_INLET4 = "FanCtrlrInlet4"
	FAN_CTRLR_INLET4_AVG = "FanCtrlrInlet4Avg"
	FAN_CTRLR_INLET4_MAX = "FanCtrlrInlet4Max"
	FAN_CTRLR_INLET4_MIN = "FanCtrlrInlet4Min"
	ID = "Id"
	MAIN_BOARD_OUTLET1 = "MainBoardOutlet1"
	MAIN_BOARD_OUTLET1_AVG = "MainBoardOutlet1Avg"
	MAIN_BOARD_OUTLET1_MAX = "MainBoardOutlet1Max"
	MAIN_BOARD_OUTLET1_MIN = "MainBoardOutlet1Min"
	MAIN_BOARD_OUTLET2 = "MainBoardOutlet2"
	MAIN_BOARD_OUTLET2_AVG = "MainBoardOutlet2Avg"
	MAIN_BOARD_OUTLET2_MAX = "MainBoardOutlet2Max"
	MAIN_BOARD_OUTLET2_MIN = "MainBoardOutlet2Min"
	MOST_RECENT = "MostRecent"
	PSU_CTRLR_INLET1 = "PsuCtrlrInlet1"
	PSU_CTRLR_INLET1_AVG = "PsuCtrlrInlet1Avg"
	PSU_CTRLR_INLET1_MAX = "PsuCtrlrInlet1Max"
	PSU_CTRLR_INLET1_MIN = "PsuCtrlrInlet1Min"
	PSU_CTRLR_INLET2 = "PsuCtrlrInlet2"
	PSU_CTRLR_INLET2_AVG = "PsuCtrlrInlet2Avg"
	PSU_CTRLR_INLET2_MAX = "PsuCtrlrInlet2Max"
	PSU_CTRLR_INLET2_MIN = "PsuCtrlrInlet2Min"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"

	CONST_FAN_CTRLR_INLET1_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET1_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET1_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET1_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET2_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET2_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET2_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET2_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET3_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET3_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET3_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET3_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET4_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET4_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET4_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_FAN_CTRLR_INLET4_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_MAIN_BOARD_OUTLET1_NOT_APPLICABLE = "not-applicable"
	CONST_MAIN_BOARD_OUTLET1_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_MAIN_BOARD_OUTLET1_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_MAIN_BOARD_OUTLET1_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_MAIN_BOARD_OUTLET2_NOT_APPLICABLE = "not-applicable"
	CONST_MAIN_BOARD_OUTLET2_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_MAIN_BOARD_OUTLET2_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_MAIN_BOARD_OUTLET2_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_PSU_CTRLR_INLET1_NOT_APPLICABLE = "not-applicable"
	CONST_PSU_CTRLR_INLET1_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_PSU_CTRLR_INLET1_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_PSU_CTRLR_INLET1_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_PSU_CTRLR_INLET2_NOT_APPLICABLE = "not-applicable"
	CONST_PSU_CTRLR_INLET2_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_PSU_CTRLR_INLET2_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_PSU_CTRLR_INLET2_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
