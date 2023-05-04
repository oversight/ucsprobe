import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPhysDevicesPerBoard(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPhysDevicesPerBoard")

	@staticmethod
	def ClassId():
		return "equipmentPhysDevicesPerBoard"

	DN = "Dn"
	NUM_OF_CPU = "NumOfCpu"
	NUM_OF_DIMM = "NumOfDimm"
	NUM_OF_LOCAL_DISK = "NumOfLocalDisk"
	NUM_OF_STORAGE_CONTROLLER = "NumOfStorageController"
	NUM_OFADAPTOR = "NumOfadaptor"
	RN = "Rn"
	STATUS = "Status"

