import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwNFExporterRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwNFExporterRef")

	@staticmethod
	def ClassId():
		return "swNFExporterRef"

	DN = "Dn"
	NAME = "Name"
	PEER_DN = "PeerDn"
	RN = "Rn"
	STATUS = "Status"

