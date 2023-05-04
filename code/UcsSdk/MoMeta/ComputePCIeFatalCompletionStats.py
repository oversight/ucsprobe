import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePCIeFatalCompletionStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePCIeFatalCompletionStats")

	@staticmethod
	def ClassId():
		return "computePCIeFatalCompletionStats"

	_ABORT_ERRORS = "AbortErrors"
	_ABORT_ERRORS15_MIN = "AbortErrors15Min"
	_ABORT_ERRORS15_MIN_H = "AbortErrors15MinH"
	_ABORT_ERRORS1_DAY = "AbortErrors1Day"
	_ABORT_ERRORS1_DAY_H = "AbortErrors1DayH"
	_ABORT_ERRORS1_HOUR = "AbortErrors1Hour"
	_ABORT_ERRORS1_HOUR_H = "AbortErrors1HourH"
	_ABORT_ERRORS1_WEEK = "AbortErrors1Week"
	_ABORT_ERRORS1_WEEK_H = "AbortErrors1WeekH"
	_ABORT_ERRORS2_WEEKS = "AbortErrors2Weeks"
	_ABORT_ERRORS2_WEEKS_H = "AbortErrors2WeeksH"
	_TIMEOUT_ERRORS = "TimeoutErrors"
	_TIMEOUT_ERRORS15_MIN = "TimeoutErrors15Min"
	_TIMEOUT_ERRORS15_MIN_H = "TimeoutErrors15MinH"
	_TIMEOUT_ERRORS1_DAY = "TimeoutErrors1Day"
	_TIMEOUT_ERRORS1_DAY_H = "TimeoutErrors1DayH"
	_TIMEOUT_ERRORS1_HOUR = "TimeoutErrors1Hour"
	_TIMEOUT_ERRORS1_HOUR_H = "TimeoutErrors1HourH"
	_TIMEOUT_ERRORS1_WEEK = "TimeoutErrors1Week"
	_TIMEOUT_ERRORS1_WEEK_H = "TimeoutErrors1WeekH"
	_TIMEOUT_ERRORS2_WEEKS = "TimeoutErrors2Weeks"
	_TIMEOUT_ERRORS2_WEEKS_H = "TimeoutErrors2WeeksH"
	DN = "Dn"
	INTERVALS = "Intervals"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UNEXPECTED_ERRORS = "UnexpectedErrors"
	UNEXPECTED_ERRORS15_MIN = "UnexpectedErrors15Min"
	UNEXPECTED_ERRORS15_MIN_H = "UnexpectedErrors15MinH"
	UNEXPECTED_ERRORS1_DAY = "UnexpectedErrors1Day"
	UNEXPECTED_ERRORS1_DAY_H = "UnexpectedErrors1DayH"
	UNEXPECTED_ERRORS1_HOUR = "UnexpectedErrors1Hour"
	UNEXPECTED_ERRORS1_HOUR_H = "UnexpectedErrors1HourH"
	UNEXPECTED_ERRORS1_WEEK = "UnexpectedErrors1Week"
	UNEXPECTED_ERRORS1_WEEK_H = "UnexpectedErrors1WeekH"
	UNEXPECTED_ERRORS2_WEEKS = "UnexpectedErrors2Weeks"
	UNEXPECTED_ERRORS2_WEEKS_H = "UnexpectedErrors2WeeksH"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
