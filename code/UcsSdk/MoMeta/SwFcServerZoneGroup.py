import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwFcServerZoneGroup(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwFcServerZoneGroup")

	@staticmethod
	def ClassId():
		return "swFcServerZoneGroup"

	DN = "Dn"
	EP_DN = "EpDn"
	ID = "Id"
	LC = "Lc"
	NAME = "Name"
	PEER_DN = "PeerDn"
	RN = "Rn"
	SERVER_DN = "ServerDn"
	STATUS = "Status"

	CONST_LC_ALLOCATED = "allocated"
	CONST_LC_AVAILABLE = "available"
	CONST_LC_DEALLOCATED = "deallocated"
	CONST_LC_REPURPOSED = "repurposed"
