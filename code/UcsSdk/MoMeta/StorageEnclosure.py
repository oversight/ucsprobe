import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageEnclosure(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageEnclosure")

	@staticmethod
	def ClassId():
		return "storageEnclosure"

	DN = "Dn"
	ID = "Id"
	LC = "Lc"
	MODEL = "Model"
	NUM_SLOTS = "NumSlots"
	REVISION = "Revision"
	RN = "Rn"
	SERIAL = "Serial"
	STATUS = "Status"
	VENDOR = "Vendor"

	CONST_LC_ALLOCATED = "allocated"
	CONST_LC_AVAILABLE = "available"
	CONST_LC_DEALLOCATED = "deallocated"
	CONST_LC_REPURPOSED = "repurposed"
