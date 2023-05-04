import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwVirtL3Intf(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwVirtL3Intf")

	@staticmethod
	def ClassId():
		return "swVirtL3Intf"

	DN = "Dn"
	IP_ADDRESS = "IpAddress"
	NAME = "Name"
	NETMASK = "Netmask"
	RN = "Rn"
	STATUS = "Status"
	VLAN_ID = "VlanId"

