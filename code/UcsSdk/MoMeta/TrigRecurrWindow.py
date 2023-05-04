import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TrigRecurrWindow(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"TrigRecurrWindow")

	@staticmethod
	def ClassId():
		return "trigRecurrWindow"

	CONCUR_CAP = "ConcurCap"
	DAY = "Day"
	DN = "Dn"
	HOUR = "Hour"
	JOB_COUNT = "JobCount"
	MINUTE = "Minute"
	NAME = "Name"
	PROC_BREAK = "ProcBreak"
	PROC_CAP = "ProcCap"
	RN = "Rn"
	STATUS = "Status"
	TIME_CAP = "TimeCap"

	CONST_CONCUR_CAP_UNLIMITED = "unlimited"
	CONST_DAY_FRIDAY = "Friday"
	CONST_DAY_MONDAY = "Monday"
	CONST_DAY_SATURDAY = "Saturday"
	CONST_DAY_SUNDAY = "Sunday"
	CONST_DAY_THURSDAY = "Thursday"
	CONST_DAY_TUESDAY = "Tuesday"
	CONST_DAY_WEDNESDAY = "Wednesday"
	CONST_DAY_EVEN_DAY = "even-day"
	CONST_DAY_EVERY_DAY = "every-day"
	CONST_DAY_ODD_DAY = "odd-day"
	CONST_PROC_BREAK_NONE = "none"
	CONST_PROC_CAP_UNLIMITED = "unlimited"
	CONST_TIME_CAP_NONE = "none"
