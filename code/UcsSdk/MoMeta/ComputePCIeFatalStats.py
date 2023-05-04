import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePCIeFatalStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePCIeFatalStats")

	@staticmethod
	def ClassId():
		return "computePCIeFatalStats"

	ACS_VIOLATION_ERRORS = "AcsViolationErrors"
	ACS_VIOLATION_ERRORS15_MIN = "AcsViolationErrors15Min"
	ACS_VIOLATION_ERRORS15_MIN_H = "AcsViolationErrors15MinH"
	ACS_VIOLATION_ERRORS1_DAY = "AcsViolationErrors1Day"
	ACS_VIOLATION_ERRORS1_DAY_H = "AcsViolationErrors1DayH"
	ACS_VIOLATION_ERRORS1_HOUR = "AcsViolationErrors1Hour"
	ACS_VIOLATION_ERRORS1_HOUR_H = "AcsViolationErrors1HourH"
	ACS_VIOLATION_ERRORS1_WEEK = "AcsViolationErrors1Week"
	ACS_VIOLATION_ERRORS1_WEEK_H = "AcsViolationErrors1WeekH"
	ACS_VIOLATION_ERRORS2_WEEKS = "AcsViolationErrors2Weeks"
	ACS_VIOLATION_ERRORS2_WEEKS_H = "AcsViolationErrors2WeeksH"
	DN = "Dn"
	INTERVALS = "Intervals"
	MALFORMED_TLPERRORS = "MalformedTLPErrors"
	MALFORMED_TLPERRORS15_MIN = "MalformedTLPErrors15Min"
	MALFORMED_TLPERRORS15_MIN_H = "MalformedTLPErrors15MinH"
	MALFORMED_TLPERRORS1_DAY = "MalformedTLPErrors1Day"
	MALFORMED_TLPERRORS1_DAY_H = "MalformedTLPErrors1DayH"
	MALFORMED_TLPERRORS1_HOUR = "MalformedTLPErrors1Hour"
	MALFORMED_TLPERRORS1_HOUR_H = "MalformedTLPErrors1HourH"
	MALFORMED_TLPERRORS1_WEEK = "MalformedTLPErrors1Week"
	MALFORMED_TLPERRORS1_WEEK_H = "MalformedTLPErrors1WeekH"
	MALFORMED_TLPERRORS2_WEEKS = "MalformedTLPErrors2Weeks"
	MALFORMED_TLPERRORS2_WEEKS_H = "MalformedTLPErrors2WeeksH"
	POISONED_TLPERRORS = "PoisonedTLPErrors"
	POISONED_TLPERRORS15_MIN = "PoisonedTLPErrors15Min"
	POISONED_TLPERRORS15_MIN_H = "PoisonedTLPErrors15MinH"
	POISONED_TLPERRORS1_DAY = "PoisonedTLPErrors1Day"
	POISONED_TLPERRORS1_DAY_H = "PoisonedTLPErrors1DayH"
	POISONED_TLPERRORS1_HOUR = "PoisonedTLPErrors1Hour"
	POISONED_TLPERRORS1_HOUR_H = "PoisonedTLPErrors1HourH"
	POISONED_TLPERRORS1_WEEK = "PoisonedTLPErrors1Week"
	POISONED_TLPERRORS1_WEEK_H = "PoisonedTLPErrors1WeekH"
	POISONED_TLPERRORS2_WEEKS = "PoisonedTLPErrors2Weeks"
	POISONED_TLPERRORS2_WEEKS_H = "PoisonedTLPErrors2WeeksH"
	RN = "Rn"
	STATUS = "Status"
	SURPRISE_LINK_DOWN_ERRORS = "SurpriseLinkDownErrors"
	SURPRISE_LINK_DOWN_ERRORS15_MIN = "SurpriseLinkDownErrors15Min"
	SURPRISE_LINK_DOWN_ERRORS15_MIN_H = "SurpriseLinkDownErrors15MinH"
	SURPRISE_LINK_DOWN_ERRORS1_DAY = "SurpriseLinkDownErrors1Day"
	SURPRISE_LINK_DOWN_ERRORS1_DAY_H = "SurpriseLinkDownErrors1DayH"
	SURPRISE_LINK_DOWN_ERRORS1_HOUR = "SurpriseLinkDownErrors1Hour"
	SURPRISE_LINK_DOWN_ERRORS1_HOUR_H = "SurpriseLinkDownErrors1HourH"
	SURPRISE_LINK_DOWN_ERRORS1_WEEK = "SurpriseLinkDownErrors1Week"
	SURPRISE_LINK_DOWN_ERRORS1_WEEK_H = "SurpriseLinkDownErrors1WeekH"
	SURPRISE_LINK_DOWN_ERRORS2_WEEKS = "SurpriseLinkDownErrors2Weeks"
	SURPRISE_LINK_DOWN_ERRORS2_WEEKS_H = "SurpriseLinkDownErrors2WeeksH"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
