import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorHostethHwAddrCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorHostethHwAddrCap")

	@staticmethod
	def ClassId():
		return "adaptorHostethHwAddrCap"

	DN = "Dn"
	MAC_OFFSET1 = "MacOffset1"
	MAC_OFFSET2 = "MacOffset2"
	RN = "Rn"
	STATUS = "Status"

