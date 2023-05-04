import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageDrive(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageDrive")

	@staticmethod
	def ClassId():
		return "storageDrive"

	DN = "Dn"
	ID = "Id"
	MODEL = "Model"
	PCI_ADDR = "PciAddr"
	REVISION = "Revision"
	RN = "Rn"
	SERIAL = "Serial"
	STATUS = "Status"
	VENDOR = "Vendor"

