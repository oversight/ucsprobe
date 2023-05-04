import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentFexEnvStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentFexEnvStatsHist")

	@staticmethod
	def ClassId():
		return "equipmentFexEnvStatsHist"

	DIE1 = "Die1"
	DIE1_AVG = "Die1Avg"
	DIE1_MAX = "Die1Max"
	DIE1_MIN = "Die1Min"
	DN = "Dn"
	ID = "Id"
	INLET = "Inlet"
	INLET1 = "Inlet1"
	INLET1_AVG = "Inlet1Avg"
	INLET1_MAX = "Inlet1Max"
	INLET1_MIN = "Inlet1Min"
	INLET_AVG = "InletAvg"
	INLET_MAX = "InletMax"
	INLET_MIN = "InletMin"
	MOST_RECENT = "MostRecent"
	OUTLET1 = "Outlet1"
	OUTLET1_AVG = "Outlet1Avg"
	OUTLET1_MAX = "Outlet1Max"
	OUTLET1_MIN = "Outlet1Min"
	OUTLET2 = "Outlet2"
	OUTLET2_AVG = "Outlet2Avg"
	OUTLET2_MAX = "Outlet2Max"
	OUTLET2_MIN = "Outlet2Min"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"

	CONST_DIE1_N_A = "N/A"
	CONST_DIE1_AVG_N_A = "N/A"
	CONST_DIE1_MAX_N_A = "N/A"
	CONST_DIE1_MIN_N_A = "N/A"
	CONST_INLET_N_A = "N/A"
	CONST_INLET1_N_A = "N/A"
	CONST_INLET1_AVG_N_A = "N/A"
	CONST_INLET1_MAX_N_A = "N/A"
	CONST_INLET1_MIN_N_A = "N/A"
	CONST_INLET_AVG_N_A = "N/A"
	CONST_INLET_MAX_N_A = "N/A"
	CONST_INLET_MIN_N_A = "N/A"
	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_OUTLET1_N_A = "N/A"
	CONST_OUTLET1_AVG_N_A = "N/A"
	CONST_OUTLET1_MAX_N_A = "N/A"
	CONST_OUTLET1_MIN_N_A = "N/A"
	CONST_OUTLET2_N_A = "N/A"
	CONST_OUTLET2_AVG_N_A = "N/A"
	CONST_OUTLET2_MAX_N_A = "N/A"
	CONST_OUTLET2_MIN_N_A = "N/A"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
