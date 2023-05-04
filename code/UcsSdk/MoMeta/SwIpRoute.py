import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwIpRoute(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwIpRoute")

	@staticmethod
	def ClassId():
		return "swIpRoute"

	DESTINATION_IP = "DestinationIp"
	DESTINATION_NETMASK = "DestinationNetmask"
	DN = "Dn"
	NAME = "Name"
	PEER_DN = "PeerDn"
	PREFIX = "Prefix"
	RN = "Rn"
	ROUTE_IP = "RouteIP"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"

	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
