import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TrigTriggered(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"TrigTriggered")

	@staticmethod
	def ClassId():
		return "trigTriggered"

	DN = "Dn"
	JOB_COUNT = "JobCount"
	OPER_STATE = "OperState"
	ORDER = "Order"
	RN = "Rn"
	STATUS = "Status"
	TR_DN = "TrDn"
	TR_ID = "TrId"

	CONST_OPER_STATE_FAILED = "failed"
	CONST_OPER_STATE_IN_PROGRESS = "in-progress"
	CONST_OPER_STATE_PENDING = "pending"
	CONST_OPER_STATE_TRIGGERED = "triggered"
