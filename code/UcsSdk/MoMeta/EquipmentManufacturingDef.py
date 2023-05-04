import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentManufacturingDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentManufacturingDef")

	@staticmethod
	def ClassId():
		return "equipmentManufacturingDef"

	CAPTION = "Caption"
	CLEI = "Clei"
	DESCR = "Descr"
	DESCRIPTION = "Description"
	DN = "Dn"
	FRU_MAJOR_TYPE = "FruMajorType"
	FRU_MINOR_TYPE = "FruMinorType"
	NAME = "Name"
	OEM_NAME = "OemName"
	OEM_PART_NUMBER = "OemPartNumber"
	PART_NUMBER = "PartNumber"
	PID = "Pid"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SERIES = "Series"
	SKU = "Sku"
	STATUS = "Status"
	VENDOR_EQUIPMENT_TYPE = "VendorEquipmentType"
	VID = "Vid"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
