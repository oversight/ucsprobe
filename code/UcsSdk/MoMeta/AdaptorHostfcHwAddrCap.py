import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorHostfcHwAddrCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorHostfcHwAddrCap")

	@staticmethod
	def ClassId():
		return "adaptorHostfcHwAddrCap"

	DN = "Dn"
	MAC_OFFSET1 = "MacOffset1"
	MAC_OFFSET2 = "MacOffset2"
	RN = "Rn"
	STATUS = "Status"
	WWN_REVERSE_MASK_A = "WwnReverseMaskA"
	WWN_REVERSE_MASK_B = "WwnReverseMaskB"
	WWNN_REVERSE_MASK_A = "WwnnReverseMaskA"
	WWNN_REVERSE_MASK_B = "WwnnReverseMaskB"

