import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CallhomePeriodicSystemInventory(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CallhomePeriodicSystemInventory")

	@staticmethod
	def ClassId():
		return "callhomePeriodicSystemInventory"

	ADMIN_STATE = "AdminState"
	DN = "Dn"
	INTERVAL_DAYS = "IntervalDays"
	LAST_DEADLINE = "LastDeadline"
	MAXIMUM_RETRY_COUNT = "MaximumRetryCount"
	MINIMUM_SEND_NOW_INTERVAL_SECONDS = "MinimumSendNowIntervalSeconds"
	NEXT_DEADLINE = "NextDeadline"
	POLL_INTERVAL_SECONDS = "PollIntervalSeconds"
	RETRY_COUNT = "RetryCount"
	RETRY_DELAY_MINUTES = "RetryDelayMinutes"
	RN = "Rn"
	SEND_NOW = "SendNow"
	STATUS = "Status"
	TIME_OF_DAY_HOUR = "TimeOfDayHour"
	TIME_OF_DAY_MINUTE = "TimeOfDayMinute"
	TIME_OF_LAST_ATTEMPT = "TimeOfLastAttempt"
	TIME_OF_LAST_SUCCESS = "TimeOfLastSuccess"

	CONST_ADMIN_STATE_OFF = "off"
	CONST_ADMIN_STATE_ON = "on"
	CONST_NEXT_DEADLINE_NEVER = "never"
	CONST_SEND_NOW_FALSE = "false"
	CONST_SEND_NOW_NO = "no"
	CONST_SEND_NOW_TRUE = "true"
	CONST_SEND_NOW_YES = "yes"
	CONST_TIME_OF_LAST_SUCCESS_NEVER = "never"
