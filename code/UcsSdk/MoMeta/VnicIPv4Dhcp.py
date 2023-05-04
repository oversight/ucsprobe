import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIPv4Dhcp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIPv4Dhcp")

	@staticmethod
	def ClassId():
		return "vnicIPv4Dhcp"

	ADDR = "Addr"
	DEF_GW = "DefGw"
	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	SUBNET = "Subnet"

