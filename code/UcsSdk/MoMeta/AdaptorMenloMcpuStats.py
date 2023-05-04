import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorMenloMcpuStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorMenloMcpuStats")

	@staticmethod
	def ClassId():
		return "adaptorMenloMcpuStats"

	DN = "Dn"
	DROP_ACL = "DropAcl"
	DROP_ACL_DELTA = "DropAclDelta"
	DROP_ACL_DELTA_AVG = "DropAclDeltaAvg"
	DROP_ACL_DELTA_MAX = "DropAclDeltaMax"
	DROP_ACL_DELTA_MIN = "DropAclDeltaMin"
	DROP_OVERRUN = "DropOverrun"
	DROP_OVERRUN_DELTA = "DropOverrunDelta"
	DROP_OVERRUN_DELTA_AVG = "DropOverrunDeltaAvg"
	DROP_OVERRUN_DELTA_MAX = "DropOverrunDeltaMax"
	DROP_OVERRUN_DELTA_MIN = "DropOverrunDeltaMin"
	DROP_RUNT = "DropRunt"
	DROP_RUNT_DELTA = "DropRuntDelta"
	DROP_RUNT_DELTA_AVG = "DropRuntDeltaAvg"
	DROP_RUNT_DELTA_MAX = "DropRuntDeltaMax"
	DROP_RUNT_DELTA_MIN = "DropRuntDeltaMin"
	INTERVALS = "Intervals"
	MENLO_MCPU_INDEX = "MenloMcpuIndex"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TRUNCATE_OVERRUN = "TruncateOverrun"
	TRUNCATE_OVERRUN_DELTA = "TruncateOverrunDelta"
	TRUNCATE_OVERRUN_DELTA_AVG = "TruncateOverrunDeltaAvg"
	TRUNCATE_OVERRUN_DELTA_MAX = "TruncateOverrunDeltaMax"
	TRUNCATE_OVERRUN_DELTA_MIN = "TruncateOverrunDeltaMin"
	UPDATE = "Update"

	CONST_MENLO_MCPU_INDEX_0 = "0"
	CONST_MENLO_MCPU_INDEX_0_A = "0_A"
	CONST_MENLO_MCPU_INDEX_0_B = "0_B"
	CONST_MENLO_MCPU_INDEX_1 = "1"
	CONST_MENLO_MCPU_INDEX_1_A = "1_A"
	CONST_MENLO_MCPU_INDEX_1_B = "1_B"
	CONST_MENLO_MCPU_INDEX_UNKNOWN = "unknown"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
