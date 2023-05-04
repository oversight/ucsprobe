import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EtherLossStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EtherLossStatsHist")

	@staticmethod
	def ClassId():
		return "etherLossStatsHist"

	_SQETEST = "SQETest"
	_SQETEST_DELTA = "SQETestDelta"
	_SQETEST_DELTA_AVG = "SQETestDeltaAvg"
	_SQETEST_DELTA_MAX = "SQETestDeltaMax"
	_SQETEST_DELTA_MIN = "SQETestDeltaMin"
	CARRIER_SENSE = "CarrierSense"
	CARRIER_SENSE_DELTA = "CarrierSenseDelta"
	CARRIER_SENSE_DELTA_AVG = "CarrierSenseDeltaAvg"
	CARRIER_SENSE_DELTA_MAX = "CarrierSenseDeltaMax"
	CARRIER_SENSE_DELTA_MIN = "CarrierSenseDeltaMin"
	DN = "Dn"
	EXCESS_COLLISION = "ExcessCollision"
	EXCESS_COLLISION_DELTA = "ExcessCollisionDelta"
	EXCESS_COLLISION_DELTA_AVG = "ExcessCollisionDeltaAvg"
	EXCESS_COLLISION_DELTA_MAX = "ExcessCollisionDeltaMax"
	EXCESS_COLLISION_DELTA_MIN = "ExcessCollisionDeltaMin"
	GIANTS = "Giants"
	GIANTS_DELTA = "GiantsDelta"
	GIANTS_DELTA_AVG = "GiantsDeltaAvg"
	GIANTS_DELTA_MAX = "GiantsDeltaMax"
	GIANTS_DELTA_MIN = "GiantsDeltaMin"
	ID = "Id"
	LATE_COLLISION = "LateCollision"
	LATE_COLLISION_DELTA = "LateCollisionDelta"
	LATE_COLLISION_DELTA_AVG = "LateCollisionDeltaAvg"
	LATE_COLLISION_DELTA_MAX = "LateCollisionDeltaMax"
	LATE_COLLISION_DELTA_MIN = "LateCollisionDeltaMin"
	MOST_RECENT = "MostRecent"
	MULTI_COLLISION = "MultiCollision"
	MULTI_COLLISION_DELTA = "MultiCollisionDelta"
	MULTI_COLLISION_DELTA_AVG = "MultiCollisionDeltaAvg"
	MULTI_COLLISION_DELTA_MAX = "MultiCollisionDeltaMax"
	MULTI_COLLISION_DELTA_MIN = "MultiCollisionDeltaMin"
	RN = "Rn"
	SINGLE_COLLISION = "SingleCollision"
	SINGLE_COLLISION_DELTA = "SingleCollisionDelta"
	SINGLE_COLLISION_DELTA_AVG = "SingleCollisionDeltaAvg"
	SINGLE_COLLISION_DELTA_MAX = "SingleCollisionDeltaMax"
	SINGLE_COLLISION_DELTA_MIN = "SingleCollisionDeltaMin"
	STATUS = "Status"
	SUSPECT = "Suspect"
	SYMBOL = "Symbol"
	SYMBOL_DELTA = "SymbolDelta"
	SYMBOL_DELTA_AVG = "SymbolDeltaAvg"
	SYMBOL_DELTA_MAX = "SymbolDeltaMax"
	SYMBOL_DELTA_MIN = "SymbolDeltaMin"
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
