import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentDowngradeConstraint(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentDowngradeConstraint")

	@staticmethod
	def ClassId():
		return "equipmentDowngradeConstraint"

	DN = "Dn"
	MIN_VER = "MinVer"
	RN = "Rn"
	STATUS = "Status"

