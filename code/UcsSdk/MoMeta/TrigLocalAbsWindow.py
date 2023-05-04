import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TrigLocalAbsWindow(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"TrigLocalAbsWindow")

	@staticmethod
	def ClassId():
		return "trigLocalAbsWindow"

	CONCUR_CAP = "ConcurCap"
	DATE = "Date"
	DN = "Dn"
	JOB_COUNT = "JobCount"
	NAME = "Name"
	PROC_BREAK = "ProcBreak"
	PROC_CAP = "ProcCap"
	RN = "Rn"
	STATUS = "Status"
	TIME_CAP = "TimeCap"

	CONST_CONCUR_CAP_UNLIMITED = "unlimited"
	CONST_PROC_BREAK_NONE = "none"
	CONST_PROC_CAP_UNLIMITED = "unlimited"
	CONST_TIME_CAP_NONE = "none"
