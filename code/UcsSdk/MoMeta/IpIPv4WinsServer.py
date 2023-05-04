import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IpIPv4WinsServer(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IpIPv4WinsServer")

	@staticmethod
	def ClassId():
		return "ipIPv4WinsServer"

	_IPV4_ADDRESS = "IPv4Address"
	DN = "Dn"
	GUID = "Guid"
	HOST = "Host"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

