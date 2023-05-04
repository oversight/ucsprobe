import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class InitiatorGroupEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"InitiatorGroupEp")

	@staticmethod
	def ClassId():
		return "initiatorGroupEp"

	DN = "Dn"
	EP_DN = "EpDn"
	ID = "Id"
	LC = "Lc"
	NAME = "Name"
	POL_NAME = "PolName"
	RMT_DISK_CFG_NAME = "RmtDiskCfgName"
	RN = "Rn"
	STATUS = "Status"

	CONST_LC_ALLOCATED = "allocated"
	CONST_LC_AVAILABLE = "available"
	CONST_LC_DEALLOCATED = "deallocated"
	CONST_LC_REPURPOSED = "repurposed"
