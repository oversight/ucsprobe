import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentBladeAggregationCapRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentBladeAggregationCapRef")

	@staticmethod
	def ClassId():
		return "equipmentBladeAggregationCapRef"

	DN = "Dn"
	IS_SUPPORTED = "IsSupported"
	RN = "Rn"
	STATUS = "Status"

	CONST_IS_SUPPORTED_FALSE = "false"
	CONST_IS_SUPPORTED_NO = "no"
	CONST_IS_SUPPORTED_TRUE = "true"
	CONST_IS_SUPPORTED_YES = "yes"
