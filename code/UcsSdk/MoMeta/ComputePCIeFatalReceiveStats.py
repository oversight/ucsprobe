import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePCIeFatalReceiveStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePCIeFatalReceiveStats")

	@staticmethod
	def ClassId():
		return "computePCIeFatalReceiveStats"

	BUFFER_OVERFLOW_ERRORS = "BufferOverflowErrors"
	BUFFER_OVERFLOW_ERRORS15_MIN = "BufferOverflowErrors15Min"
	BUFFER_OVERFLOW_ERRORS15_MIN_H = "BufferOverflowErrors15MinH"
	BUFFER_OVERFLOW_ERRORS1_DAY = "BufferOverflowErrors1Day"
	BUFFER_OVERFLOW_ERRORS1_DAY_H = "BufferOverflowErrors1DayH"
	BUFFER_OVERFLOW_ERRORS1_HOUR = "BufferOverflowErrors1Hour"
	BUFFER_OVERFLOW_ERRORS1_HOUR_H = "BufferOverflowErrors1HourH"
	BUFFER_OVERFLOW_ERRORS1_WEEK = "BufferOverflowErrors1Week"
	BUFFER_OVERFLOW_ERRORS1_WEEK_H = "BufferOverflowErrors1WeekH"
	BUFFER_OVERFLOW_ERRORS2_WEEKS = "BufferOverflowErrors2Weeks"
	BUFFER_OVERFLOW_ERRORS2_WEEKS_H = "BufferOverflowErrors2WeeksH"
	DN = "Dn"
	ERR_FATAL_ERRORS = "ErrFatalErrors"
	ERR_FATAL_ERRORS15_MIN = "ErrFatalErrors15Min"
	ERR_FATAL_ERRORS15_MIN_H = "ErrFatalErrors15MinH"
	ERR_FATAL_ERRORS1_DAY = "ErrFatalErrors1Day"
	ERR_FATAL_ERRORS1_DAY_H = "ErrFatalErrors1DayH"
	ERR_FATAL_ERRORS1_HOUR = "ErrFatalErrors1Hour"
	ERR_FATAL_ERRORS1_HOUR_H = "ErrFatalErrors1HourH"
	ERR_FATAL_ERRORS1_WEEK = "ErrFatalErrors1Week"
	ERR_FATAL_ERRORS1_WEEK_H = "ErrFatalErrors1WeekH"
	ERR_FATAL_ERRORS2_WEEKS = "ErrFatalErrors2Weeks"
	ERR_FATAL_ERRORS2_WEEKS_H = "ErrFatalErrors2WeeksH"
	ERR_NON_FATAL_ERRORS = "ErrNonFatalErrors"
	ERR_NON_FATAL_ERRORS15_MIN = "ErrNonFatalErrors15Min"
	ERR_NON_FATAL_ERRORS15_MIN_H = "ErrNonFatalErrors15MinH"
	ERR_NON_FATAL_ERRORS1_DAY = "ErrNonFatalErrors1Day"
	ERR_NON_FATAL_ERRORS1_DAY_H = "ErrNonFatalErrors1DayH"
	ERR_NON_FATAL_ERRORS1_HOUR = "ErrNonFatalErrors1Hour"
	ERR_NON_FATAL_ERRORS1_HOUR_H = "ErrNonFatalErrors1HourH"
	ERR_NON_FATAL_ERRORS1_WEEK = "ErrNonFatalErrors1Week"
	ERR_NON_FATAL_ERRORS1_WEEK_H = "ErrNonFatalErrors1WeekH"
	ERR_NON_FATAL_ERRORS2_WEEKS = "ErrNonFatalErrors2Weeks"
	ERR_NON_FATAL_ERRORS2_WEEKS_H = "ErrNonFatalErrors2WeeksH"
	INTERVALS = "Intervals"
	RN = "Rn"
	STATUS = "Status"
	SUSPECT = "Suspect"
	THRESHOLDED = "Thresholded"
	TIME_COLLECTED = "TimeCollected"
	UNSUPPORTED_REQUEST_ERRORS = "UnsupportedRequestErrors"
	UNSUPPORTED_REQUEST_ERRORS15_MIN = "UnsupportedRequestErrors15Min"
	UNSUPPORTED_REQUEST_ERRORS15_MIN_H = "UnsupportedRequestErrors15MinH"
	UNSUPPORTED_REQUEST_ERRORS1_DAY = "UnsupportedRequestErrors1Day"
	UNSUPPORTED_REQUEST_ERRORS1_DAY_H = "UnsupportedRequestErrors1DayH"
	UNSUPPORTED_REQUEST_ERRORS1_HOUR = "UnsupportedRequestErrors1Hour"
	UNSUPPORTED_REQUEST_ERRORS1_HOUR_H = "UnsupportedRequestErrors1HourH"
	UNSUPPORTED_REQUEST_ERRORS1_WEEK = "UnsupportedRequestErrors1Week"
	UNSUPPORTED_REQUEST_ERRORS1_WEEK_H = "UnsupportedRequestErrors1WeekH"
	UNSUPPORTED_REQUEST_ERRORS2_WEEKS = "UnsupportedRequestErrors2Weeks"
	UNSUPPORTED_REQUEST_ERRORS2_WEEKS_H = "UnsupportedRequestErrors2WeeksH"
	UPDATE = "Update"

	CONST_SUSPECT_FALSE = "false"
	CONST_SUSPECT_NO = "no"
	CONST_SUSPECT_TRUE = "true"
	CONST_SUSPECT_YES = "yes"
