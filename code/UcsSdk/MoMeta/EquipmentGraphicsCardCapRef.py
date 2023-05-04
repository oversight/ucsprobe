import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentGraphicsCardCapRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentGraphicsCardCapRef")

	@staticmethod
	def ClassId():
		return "equipmentGraphicsCardCapRef"

	DN = "Dn"
	MODEL = "Model"
	REVISION = "Revision"
	RN = "Rn"
	STATUS = "Status"
	VENDOR = "Vendor"

