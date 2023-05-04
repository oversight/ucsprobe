import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwNetflowMonitorRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwNetflowMonitorRef")

	@staticmethod
	def ClassId():
		return "swNetflowMonitorRef"

	DIRECTION = "Direction"
	DN = "Dn"
	KEY_TYPE = "KeyType"
	NAME = "Name"
	RN = "Rn"
	SOURCE_DN = "SourceDn"
	STATUS = "Status"

	CONST_DIRECTION_RECEIVE = "receive"
	CONST_DIRECTION_TRANSMIT = "transmit"
	CONST_KEY_TYPE_IPV4KEYS = "ipv4keys"
	CONST_KEY_TYPE_IPV6KEYS = "ipv6keys"
	CONST_KEY_TYPE_L2KEYS = "l2keys"
