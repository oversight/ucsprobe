import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwNetflowRecordDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwNetflowRecordDef")

	@staticmethod
	def ClassId():
		return "swNetflowRecordDef"

	DN = "Dn"
	IPV4KEYS = "Ipv4keys"
	IPV6KEYS = "Ipv6keys"
	KEY_TYPE = "KeyType"
	L2KEYS = "L2keys"
	LIFE_CYCLE = "LifeCycle"
	NAME = "Name"
	NONKEYS = "Nonkeys"
	PEER_DN = "PeerDn"
	PROTOCOL = "Protocol"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_KEY_TYPE_IPV4KEYS = "ipv4keys"
	CONST_KEY_TYPE_IPV6KEYS = "ipv6keys"
	CONST_KEY_TYPE_L2KEYS = "l2keys"
	CONST_LIFE_CYCLE_DELETED = "deleted"
	CONST_LIFE_CYCLE_NEW = "new"
	CONST_LIFE_CYCLE_NORMAL = "normal"
	CONST_PROTOCOL_NETFLOW = "netflow"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
