import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorUplinkHwAddrCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorUplinkHwAddrCap")

	@staticmethod
	def ClassId():
		return "adaptorUplinkHwAddrCap"

	DN = "Dn"
	LLDP_MAC_OFFSET1 = "LldpMacOffset1"
	LLDP_MAC_OFFSET2 = "LldpMacOffset2"
	MAC_OFFSET1 = "MacOffset1"
	MAC_OFFSET2 = "MacOffset2"
	MAC_OFFSET_SUB00 = "MacOffsetSub00"
	MAC_OFFSET_SUB01 = "MacOffsetSub01"
	MAC_OFFSET_SUB02 = "MacOffsetSub02"
	MAC_OFFSET_SUB03 = "MacOffsetSub03"
	MAC_OFFSET_SUB10 = "MacOffsetSub10"
	MAC_OFFSET_SUB11 = "MacOffsetSub11"
	MAC_OFFSET_SUB12 = "MacOffsetSub12"
	MAC_OFFSET_SUB13 = "MacOffsetSub13"
	RN = "Rn"
	STATUS = "Status"

