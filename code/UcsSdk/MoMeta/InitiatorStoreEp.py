import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class InitiatorStoreEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"InitiatorStoreEp")

	@staticmethod
	def ClassId():
		return "initiatorStoreEp"

	DN = "Dn"
	EP_DN = "EpDn"
	ID = "Id"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_TYPE_DEDICATED = "dedicated"
	CONST_TYPE_POLICY = "policy"
	CONST_TYPE_SHARED = "shared"
