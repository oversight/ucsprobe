import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEthPortBySizeLargeStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEthPortBySizeLargeStats")

	@staticmethod
	def ClassId():
		return "adaptorEthPortBySizeLargeStats"

	DN = "Dn"
	GREATER_THAN_OR_EQUAL_TO9216 = "GreaterThanOrEqualTo9216"
	GREATER_THAN_OR_EQUAL_TO9216_DELTA = "GreaterThanOrEqualTo9216Delta"
	GREATER_THAN_OR_EQUAL_TO9216_DELTA_AVG = "GreaterThanOrEqualTo9216DeltaAvg"
	GREATER_THAN_OR_EQUAL_TO9216_DELTA_MAX = "GreaterThanOrEqualTo9216DeltaMax"
	GREATER_THAN_OR_EQUAL_TO9216_DELTA_MIN = "GreaterThanOrEqualTo9216DeltaMin"
	INTERVALS = "Intervals"
	LESS_THAN2048 = "LessThan2048"
	LESS_THAN2048_DELTA = "LessThan2048Delta"
	LESS_THAN2048_DELTA_AVG = "LessThan2048DeltaAvg"
	LESS_THAN2048_DELTA_MAX = "LessThan2048DeltaMax"
	LESS_THAN2048_DELTA_MIN = "LessThan2048DeltaMin"
	LESS_THAN4096 = "LessThan4096"
	LESS_THAN4096_DELTA = "LessThan4096Delta"
	LESS_THAN4096_DELTA_AVG = "LessThan4096DeltaAvg"
	LESS_THAN4096_DELTA_MAX = "LessThan4096DeltaMax"
	LESS_THAN4096_DELTA_MIN = "LessThan4096DeltaMin"
	LESS_THAN8192 = "LessThan8192"
	LESS_THAN8192_DELTA = "LessThan8192Delta"
	LESS_THAN8192_DELTA_AVG = "LessThan8192DeltaAvg"
	LESS_THAN8192_DELTA_MAX = "LessThan8192DeltaMax"
	LESS_THAN8192_DELTA_MIN = "LessThan8192DeltaMin"
	LESS_THAN9216 = "LessThan9216"
	LESS_THAN9216_DELTA = "LessThan9216Delta"
	LESS_THAN9216_DELTA_AVG = "LessThan9216DeltaAvg"
	LESS_THAN9216_DELTA_MAX = "LessThan9216DeltaMax"
	LESS_THAN9216_DELTA_MIN = "LessThan9216DeltaMin"
	LESS_THAN_OR_EQUAL_TO1518 = "LessThanOrEqualTo1518"
	LESS_THAN_OR_EQUAL_TO1518_DELTA = "LessThanOrEqualTo1518Delta"
	LESS_THAN_OR_EQUAL_TO1518_DELTA_AVG = "LessThanOrEqualTo1518DeltaAvg"
	LESS_THAN_OR_EQUAL_TO1518_DELTA_MAX = "LessThanOrEqualTo1518DeltaMax"
	LESS_THAN_OR_EQUAL_TO1518_DELTA_MIN = "LessThanOrEqualTo1518DeltaMin"
	NO_BREAKDOWN_GREATER_THAN1518 = "NoBreakdownGreaterThan1518"
	NO_BREAKDOWN_GREATER_THAN1518_DELTA = "NoBreakdownGreaterThan1518Delta"
	NO_BREAKDOWN_GREATER_THAN1518_DELTA_AVG = "NoBreakdownGreaterThan1518DeltaAvg"
	NO_BREAKDOWN_GREATER_THAN1518_DELTA_MAX = "NoBreakdownGreaterThan1518DeltaMax"
	NO_BREAKDOWN_GREATER_THAN1518_DELTA_MIN = "NoBreakdownGreaterThan1518DeltaMin"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	TRAFFIC_DIRECTION = "TrafficDirection"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
	CONST_TRAFFIC_DIRECTION_RX = "rx"
	CONST_TRAFFIC_DIRECTION_TX = "tx"
	CONST_TRAFFIC_DIRECTION_UNKNOWN = "unknown"
