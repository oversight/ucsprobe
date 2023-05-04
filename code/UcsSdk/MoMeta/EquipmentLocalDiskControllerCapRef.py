import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentLocalDiskControllerCapRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentLocalDiskControllerCapRef")

	@staticmethod
	def ClassId():
		return "equipmentLocalDiskControllerCapRef"

	DN = "Dn"
	IS_SUPPORTED = "IsSupported"
	MODEL = "Model"
	REVISION = "Revision"
	RN = "Rn"
	STATUS = "Status"
	VENDOR = "Vendor"

	CONST_IS_SUPPORTED_NO = "no"
	CONST_IS_SUPPORTED_YES = "yes"
