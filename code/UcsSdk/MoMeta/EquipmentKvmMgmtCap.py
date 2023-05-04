import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentKvmMgmtCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentKvmMgmtCap")

	@staticmethod
	def ClassId():
		return "equipmentKvmMgmtCap"

	DN = "Dn"
	IS_SUPPORTED = "IsSupported"
	MIN_CIMC_VERSION = "MinCimcVersion"
	RN = "Rn"
	STATUS = "Status"

	CONST_IS_SUPPORTED_NO = "no"
	CONST_IS_SUPPORTED_YES = "yes"
