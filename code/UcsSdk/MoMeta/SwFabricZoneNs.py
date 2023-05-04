import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwFabricZoneNs(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwFabricZoneNs")

	@staticmethod
	def ClassId():
		return "swFabricZoneNs"

	ALLOC_STATUS = "AllocStatus"
	DN = "Dn"
	LIMIT = "Limit"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	ZONE_COUNT = "ZoneCount"

	CONST_ALLOC_STATUS_AVAILABLE = "available"
	CONST_ALLOC_STATUS_FULL = "full"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
