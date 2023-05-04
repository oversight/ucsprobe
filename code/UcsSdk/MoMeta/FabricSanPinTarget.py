import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricSanPinTarget(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricSanPinTarget")

	@staticmethod
	def ClassId():
		return "fabricSanPinTarget"

	DN = "Dn"
	EP_DN = "EpDn"
	FABRIC_ID = "FabricId"
	RN = "Rn"
	STATUS = "Status"
	TARGET_STATUS = "TargetStatus"

	CONST_FABRIC_ID_A = "A"
	CONST_FABRIC_ID_B = "B"
	CONST_FABRIC_ID_NONE = "NONE"
	CONST_FABRIC_ID_DUAL = "dual"
	CONST_TARGET_STATUS_INVALID = "invalid"
	CONST_TARGET_STATUS_VALID = "valid"
