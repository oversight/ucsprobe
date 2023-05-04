import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentInbandMgmtCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentInbandMgmtCap")

	@staticmethod
	def ClassId():
		return "equipmentInbandMgmtCap"

	DN = "Dn"
	IS_SUPPORTED = "IsSupported"
	MIN_CIMC_VERSION = "MinCimcVersion"
	MIN_CMC_VERSION = "MinCmcVersion"
	RN = "Rn"
	STATUS = "Status"

	CONST_IS_SUPPORTED_NO = "no"
	CONST_IS_SUPPORTED_YES = "yes"
