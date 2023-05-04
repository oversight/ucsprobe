import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class NetworkIfStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"NetworkIfStats")

	@staticmethod
	def ClassId():
		return "networkIfStats"

	DN = "Dn"
	IN = "In"
	OUT = "Out"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	UNITS = "Units"

	CONST_TYPE_BROADCAST = "broadcast"
	CONST_TYPE_GENERIC = "generic"
	CONST_TYPE_MULTICAST = "multicast"
	CONST_TYPE_TOTAL = "total"
	CONST_TYPE_UNICAST = "unicast"
	CONST_UNITS_OCTETS = "octets"
	CONST_UNITS_PACKETS = "packets"
	CONST_UNITS_RAW = "raw"
