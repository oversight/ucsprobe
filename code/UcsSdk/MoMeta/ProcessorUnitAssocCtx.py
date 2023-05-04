import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProcessorUnitAssocCtx(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ProcessorUnitAssocCtx")

	@staticmethod
	def ClassId():
		return "processorUnitAssocCtx"

	DN = "Dn"
	FRU_CAP_DN = "FruCapDn"
	RN = "Rn"
	STATUS = "Status"
	STEPPING = "Stepping"

	CONST_STEPPING_UNSPECIFIED = "unspecified"
