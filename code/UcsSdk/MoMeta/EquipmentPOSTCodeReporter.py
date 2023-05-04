import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPOSTCodeReporter(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPOSTCodeReporter")

	@staticmethod
	def ClassId():
		return "equipmentPOSTCodeReporter"

	BASE_CONTAINER = "BaseContainer"
	DN = "Dn"
	MODEL = "Model"
	NAME = "Name"
	REVISION = "Revision"
	RN = "Rn"
	SERIAL = "Serial"
	STATUS = "Status"
	TYPE = "Type"
	VENDOR = "Vendor"

