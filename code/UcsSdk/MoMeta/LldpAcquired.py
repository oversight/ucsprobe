import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LldpAcquired(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LldpAcquired")

	@staticmethod
	def ClassId():
		return "lldpAcquired"

	ACQTS = "Acqts"
	CHASSIS_MAC = "ChassisMac"
	DN = "Dn"
	PEER_DN = "PeerDn"
	PORT_MAC = "PortMac"
	RN = "Rn"
	STATUS = "Status"

