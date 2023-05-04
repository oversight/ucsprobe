import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class InitiatorMemberEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"InitiatorMemberEp")

	@staticmethod
	def ClassId():
		return "initiatorMemberEp"

	DN = "Dn"
	EP_DN = "EpDn"
	ID = "Id"
	RN = "Rn"
	STATUS = "Status"

