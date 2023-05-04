import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricVCon(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricVCon")

	@staticmethod
	def ClassId():
		return "fabricVCon"

	DN = "Dn"
	EQUIPMENT_DN = "EquipmentDn"
	FABRIC = "Fabric"
	ID = "Id"
	INST_TYPE = "InstType"
	PLACEMENT = "Placement"
	RN = "Rn"
	SELECT = "Select"
	SHARE = "Share"
	STATUS = "Status"
	TRANSPORT = "Transport"

	CONST_FABRIC_A = "A"
	CONST_FABRIC_B = "B"
	CONST_FABRIC_NONE = "NONE"
	CONST_FABRIC_ANY = "any"
	CONST_ID_1 = "1"
	CONST_ID_2 = "2"
	CONST_ID_3 = "3"
	CONST_ID_4 = "4"
	CONST_INST_TYPE_AUTO = "auto"
	CONST_INST_TYPE_MANUAL = "manual"
	CONST_INST_TYPE_POLICY = "policy"
	CONST_PLACEMENT_AUTO = "auto"
	CONST_PLACEMENT_PHYSICAL = "physical"
	CONST_SELECT_ALL = "all"
	CONST_SELECT_ASSIGNED_ONLY = "assigned-only"
	CONST_SELECT_DYNAMIC_ONLY = "dynamic-only"
	CONST_SELECT_EXCLUDE_DYNAMIC = "exclude-dynamic"
	CONST_SELECT_EXCLUDE_UNASSIGNED = "exclude-unassigned"
	CONST_SELECT_EXCLUDE_USNIC = "exclude-usnic"
	CONST_SELECT_UNASSIGNED_ONLY = "unassigned-only"
	CONST_SELECT_USNIC_ONLY = "usnic-only"
	CONST_SHARE_DIFFERENT_TRANSPORT = "different-transport"
	CONST_SHARE_EXCLUSIVE_ONLY = "exclusive-only"
	CONST_SHARE_EXCLUSIVE_PREFERRED = "exclusive-preferred"
	CONST_SHARE_SAME_TRANSPORT = "same-transport"
	CONST_SHARE_SHARED = "shared"
