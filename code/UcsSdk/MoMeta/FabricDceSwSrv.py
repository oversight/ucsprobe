import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricDceSwSrv(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricDceSwSrv")

	@staticmethod
	def ClassId():
		return "fabricDceSwSrv"

	DN = "Dn"
	ID = "Id"
	LOCALE = "Locale"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_ID_A = "A"
	CONST_ID_B = "B"
	CONST_ID_NONE = "NONE"
