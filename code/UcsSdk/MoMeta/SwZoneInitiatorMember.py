import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwZoneInitiatorMember(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwZoneInitiatorMember")

	@staticmethod
	def ClassId():
		return "swZoneInitiatorMember"

	DN = "Dn"
	EP_DN = "EpDn"
	LC = "Lc"
	NAME = "Name"
	PEER_DN = "PeerDn"
	RN = "Rn"
	STATUS = "Status"
	WWPN = "Wwpn"

	CONST_LC_ALLOCATED = "allocated"
	CONST_LC_AVAILABLE = "available"
	CONST_LC_DEALLOCATED = "deallocated"
	CONST_LC_REPURPOSED = "repurposed"
