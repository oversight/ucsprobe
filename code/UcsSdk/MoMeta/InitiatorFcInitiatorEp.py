import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class InitiatorFcInitiatorEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"InitiatorFcInitiatorEp")

	@staticmethod
	def ClassId():
		return "initiatorFcInitiatorEp"

	DN = "Dn"
	EP_DN = "EpDn"
	ID = "Id"
	NAME = "Name"
	PREF = "Pref"
	PROT = "Prot"
	RN = "Rn"
	STATUS = "Status"
	WWPN = "Wwpn"

	CONST_PREF_ALTERNATE = "alternate"
	CONST_PREF_PREFERRED = "preferred"
	CONST_PROT_DERIVED = "derived"
	CONST_PROT_FC = "fc"
	CONST_PROT_ISCSI = "iscsi"
