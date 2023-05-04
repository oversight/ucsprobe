import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentVersionConstraint(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentVersionConstraint")

	@staticmethod
	def ClassId():
		return "equipmentVersionConstraint"

	DN = "Dn"
	MIN_VER1 = "MinVer1"
	RN = "Rn"
	STATUS = "Status"

