import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricEthMonSrcEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricEthMonSrcEp")

	@staticmethod
	def ClassId():
		return "fabricEthMonSrcEp"

	DIRECTION = "Direction"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	SESSION = "Session"
	STATUS = "Status"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_DIRECTION_BOTH = "both"
	CONST_DIRECTION_RX = "rx"
	CONST_DIRECTION_TX = "tx"
