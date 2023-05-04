import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricIf(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricIf")

	@staticmethod
	def ClassId():
		return "fabricIf"

	ADDR = "Addr"
	DN = "Dn"
	ID = "Id"
	RN = "Rn"
	STATUS = "Status"

	CONST_ID_A = "A"
	CONST_ID_B = "B"
	CONST_ID_NONE = "NONE"
