import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwFcZoneSet(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwFcZoneSet")

	@staticmethod
	def ClassId():
		return "swFcZoneSet"

	CURRENT_ZONE_PREFIX = "CurrentZonePrefix"
	DN = "Dn"
	LC = "Lc"
	NAME = "Name"
	OLD_ZONE_PREFIX = "OldZonePrefix"
	RN = "Rn"
	STATUS = "Status"

	CONST_LC_ALLOCATED = "allocated"
	CONST_LC_AVAILABLE = "available"
	CONST_LC_DEALLOCATED = "deallocated"
	CONST_LC_REPURPOSED = "repurposed"
