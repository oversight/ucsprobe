import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPOSTCodeTemplate(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPOSTCodeTemplate")

	@staticmethod
	def ClassId():
		return "equipmentPOSTCodeTemplate"

	BASE_CONTAINER = "BaseContainer"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

