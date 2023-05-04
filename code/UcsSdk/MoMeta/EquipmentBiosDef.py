import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentBiosDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentBiosDef")

	@staticmethod
	def ClassId():
		return "equipmentBiosDef"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RESET_ON = "ResetOn"
	RN = "Rn"
	SECURE_BIOS = "SecureBios"
	STATUS = "Status"
	STORAGE_METHOD = "StorageMethod"
	UPDATE_METHOD = "UpdateMethod"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_RESET_ON_ACTIVATE = "Activate"
	CONST_RESET_ON_UNKNOWN = "Unknown"
	CONST_RESET_ON_UPDATE = "Update"
	CONST_SECURE_BIOS_NOT_SUPPORTED = "Not supported"
	CONST_SECURE_BIOS_SUPPORTED = "Supported"
	CONST_SECURE_BIOS_UNKNOWN = "Unknown"
	CONST_STORAGE_METHOD_DUAL_FLASH = "Dual Flash"
	CONST_STORAGE_METHOD_SINGLE_FLASH = "Single Flash"
	CONST_STORAGE_METHOD_UNKNOWN = "Unknown"
	CONST_UPDATE_METHOD_MANAGEMENT_CONTROLLER = "Management Controller"
	CONST_UPDATE_METHOD_PNUOS = "Pnuos"
	CONST_UPDATE_METHOD_UNKNOWN = "Unknown"
