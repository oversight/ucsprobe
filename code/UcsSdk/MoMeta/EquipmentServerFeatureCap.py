import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentServerFeatureCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentServerFeatureCap")

	@staticmethod
	def ClassId():
		return "equipmentServerFeatureCap"

	CMOS_RESET_SUPPORTED = "CmosResetSupported"
	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

	CONST_CMOS_RESET_SUPPORTED_FALSE = "false"
	CONST_CMOS_RESET_SUPPORTED_NO = "no"
	CONST_CMOS_RESET_SUPPORTED_TRUE = "true"
	CONST_CMOS_RESET_SUPPORTED_YES = "yes"
