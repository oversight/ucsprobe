import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwCardEnvStatsHist(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwCardEnvStatsHist")

	@staticmethod
	def ClassId():
		return "swCardEnvStatsHist"

	_SLOT_OUTLET1 = "SlotOutlet1"
	_SLOT_OUTLET1_AVG = "SlotOutlet1Avg"
	_SLOT_OUTLET1_MAX = "SlotOutlet1Max"
	_SLOT_OUTLET1_MIN = "SlotOutlet1Min"
	_SLOT_OUTLET2 = "SlotOutlet2"
	_SLOT_OUTLET2_AVG = "SlotOutlet2Avg"
	_SLOT_OUTLET2_MAX = "SlotOutlet2Max"
	_SLOT_OUTLET2_MIN = "SlotOutlet2Min"
	_SLOT_OUTLET3 = "SlotOutlet3"
	_SLOT_OUTLET3_AVG = "SlotOutlet3Avg"
	_SLOT_OUTLET3_MAX = "SlotOutlet3Max"
	_SLOT_OUTLET3_MIN = "SlotOutlet3Min"
	DN = "Dn"
	ID = "Id"
	MOST_RECENT = "MostRecent"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"

	CONST_SLOT_OUTLET1_NOT_APPLICABLE = "not-applicable"
	CONST_SLOT_OUTLET1_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_SLOT_OUTLET1_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_SLOT_OUTLET1_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_SLOT_OUTLET2_NOT_APPLICABLE = "not-applicable"
	CONST_SLOT_OUTLET2_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_SLOT_OUTLET2_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_SLOT_OUTLET2_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_SLOT_OUTLET3_NOT_APPLICABLE = "not-applicable"
	CONST_SLOT_OUTLET3_AVG_NOT_APPLICABLE = "not-applicable"
	CONST_SLOT_OUTLET3_MAX_NOT_APPLICABLE = "not-applicable"
	CONST_SLOT_OUTLET3_MIN_NOT_APPLICABLE = "not-applicable"
	CONST_MOST_RECENT_FALSE = "false"
	CONST_MOST_RECENT_NO = "no"
	CONST_MOST_RECENT_TRUE = "true"
	CONST_MOST_RECENT_YES = "yes"
	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
