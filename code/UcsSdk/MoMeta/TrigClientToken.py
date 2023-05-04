import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TrigClientToken(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"TrigClientToken")

	@staticmethod
	def ClassId():
		return "trigClientToken"

	ACTIVITY_TS = "ActivityTs"
	DN = "Dn"
	ID = "Id"
	OPER_STATE = "OperState"
	RN = "Rn"
	STATUS = "Status"

	CONST_OPER_STATE_EXPIRED = "expired"
	CONST_OPER_STATE_VALID = "valid"
