import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IpIpV4StaticAddr(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IpIpV4StaticAddr")

	@staticmethod
	def ClassId():
		return "ipIpV4StaticAddr"

	ADDR = "Addr"
	DEF_GW = "DefGw"
	DN = "Dn"
	PREF = "Pref"
	RN = "Rn"
	STATUS = "Status"
	SUBNET = "Subnet"

	CONST_PREF_ALTERNATE = "alternate"
	CONST_PREF_PREFERRED = "preferred"
