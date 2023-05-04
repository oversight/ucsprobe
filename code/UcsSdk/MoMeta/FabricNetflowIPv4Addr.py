import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricNetflowIPv4Addr(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricNetflowIPv4Addr")

	@staticmethod
	def ClassId():
		return "fabricNetflowIPv4Addr"

	ADDR = "Addr"
	DEF_GW = "DefGw"
	DN = "Dn"
	FABRIC_ID = "FabricId"
	RN = "Rn"
	STATUS = "Status"
	SUBNET = "Subnet"

	CONST_FABRIC_ID_A = "A"
	CONST_FABRIC_ID_B = "B"
	CONST_FABRIC_ID_NONE = "NONE"
