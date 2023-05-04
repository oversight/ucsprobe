import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentFirmwareConstraint(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentFirmwareConstraint")

	@staticmethod
	def ClassId():
		return "equipmentFirmwareConstraint"

	DN = "Dn"
	MIN_VER1 = "MinVer1"
	MIN_VER2 = "MinVer2"
	RN = "Rn"
	STATUS = "Status"

