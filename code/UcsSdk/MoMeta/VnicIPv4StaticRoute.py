import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIPv4StaticRoute(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIPv4StaticRoute")

	@staticmethod
	def ClassId():
		return "vnicIPv4StaticRoute"

	ADDR = "Addr"
	DEF_GW = "DefGw"
	DN = "Dn"
	GW_ADDR = "GwAddr"
	GW_SUBNET = "GwSubnet"
	RN = "Rn"
	STATUS = "Status"
	SUBNET = "Subnet"

