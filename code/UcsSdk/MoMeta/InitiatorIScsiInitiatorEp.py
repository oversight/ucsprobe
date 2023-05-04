import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class InitiatorIScsiInitiatorEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"InitiatorIScsiInitiatorEp")

	@staticmethod
	def ClassId():
		return "initiatorIScsiInitiatorEp"

	DN = "Dn"
	EP_DN = "EpDn"
	ID = "Id"
	IQN = "Iqn"
	NAME = "Name"
	PREF = "Pref"
	PROT = "Prot"
	RN = "Rn"
	STATUS = "Status"

	CONST_PREF_ALTERNATE = "alternate"
	CONST_PREF_PREFERRED = "preferred"
	CONST_PROT_DERIVED = "derived"
	CONST_PROT_FC = "fc"
	CONST_PROT_ISCSI = "iscsi"
