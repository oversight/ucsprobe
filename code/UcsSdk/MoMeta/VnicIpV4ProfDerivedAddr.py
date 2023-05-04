import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIpV4ProfDerivedAddr(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIpV4ProfDerivedAddr")

	@staticmethod
	def ClassId():
		return "vnicIpV4ProfDerivedAddr"

	ADDR = "Addr"
	DEF_GW = "DefGw"
	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	SUBNET = "Subnet"

