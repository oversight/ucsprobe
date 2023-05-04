import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsZoneInitiatorMember(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsZoneInitiatorMember")

	@staticmethod
	def ClassId():
		return "lsZoneInitiatorMember"

	DN = "Dn"
	EP_DN = "EpDn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	USR_LBL = "UsrLbl"
	WWPN = "Wwpn"

