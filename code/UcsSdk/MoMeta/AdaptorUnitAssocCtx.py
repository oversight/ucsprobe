import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorUnitAssocCtx(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorUnitAssocCtx")

	@staticmethod
	def ClassId():
		return "adaptorUnitAssocCtx"

	DN = "Dn"
	FRU_CAP_DN = "FruCapDn"
	ID = "Id"
	PCI_ADDR = "PciAddr"
	RN = "Rn"
	STATUS = "Status"

