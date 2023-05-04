import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class InitiatorUnitEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"InitiatorUnitEp")

	@staticmethod
	def ClassId():
		return "initiatorUnitEp"

	BOOT = "Boot"
	DN = "Dn"
	EP_DN = "EpDn"
	HA = "Ha"
	ID = "Id"
	ITEM_DN = "ItemDn"
	LC = "Lc"
	PHY_ID = "PhyId"
	PROT = "Prot"
	RN = "Rn"
	STATUS = "Status"

	CONST_BOOT_FALSE = "false"
	CONST_BOOT_NO = "no"
	CONST_BOOT_TRUE = "true"
	CONST_BOOT_YES = "yes"
	CONST_LC_ALLOCATED = "allocated"
	CONST_LC_AVAILABLE = "available"
	CONST_LC_DEALLOCATED = "deallocated"
	CONST_LC_REPURPOSED = "repurposed"
	CONST_PROT_DERIVED = "derived"
	CONST_PROT_FC = "fc"
	CONST_PROT_ISCSI = "iscsi"
