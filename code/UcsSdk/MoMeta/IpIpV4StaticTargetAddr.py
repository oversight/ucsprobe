import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IpIpV4StaticTargetAddr(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IpIpV4StaticTargetAddr")

	@staticmethod
	def ClassId():
		return "ipIpV4StaticTargetAddr"

	ADDR = "Addr"
	DEF_GW = "DefGw"
	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	SUBNET = "Subnet"

