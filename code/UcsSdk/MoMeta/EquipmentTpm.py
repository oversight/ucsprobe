import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentTpm(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentTpm")

	@staticmethod
	def ClassId():
		return "equipmentTpm"

	ACTIVE_STATUS = "ActiveStatus"
	DN = "Dn"
	ENABLED_STATUS = "EnabledStatus"
	ID = "Id"
	MODEL = "Model"
	OWNERSHIP = "Ownership"
	PASSWORD_STATE = "PasswordState"
	PRESENCE = "Presence"
	REVISION = "Revision"
	RN = "Rn"
	SERIAL = "Serial"
	STATUS = "Status"
	TPM_REVISION = "TpmRevision"
	TYPE = "Type"
	VENDOR = "Vendor"

	CONST_ACTIVE_STATUS_ACTIVATED = "activated"
	CONST_ACTIVE_STATUS_DEACTIVATED = "deactivated"
	CONST_ACTIVE_STATUS_UNKNOWN = "unknown"
	CONST_ENABLED_STATUS_DISABLED = "disabled"
	CONST_ENABLED_STATUS_ENABLED = "enabled"
	CONST_ENABLED_STATUS_UNKNOWN = "unknown"
	CONST_OWNERSHIP_OWNED = "owned"
	CONST_OWNERSHIP_UNKNOWN = "unknown"
	CONST_OWNERSHIP_UNOWNED = "unowned"
	CONST_PASSWORD_STATE_NOT_SET = "not-set"
	CONST_PASSWORD_STATE_SET = "set"
	CONST_PASSWORD_STATE_UNKNOWN = "unknown"
	CONST_PRESENCE_EMPTY = "empty"
	CONST_PRESENCE_EQUIPPED = "equipped"
	CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
	CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
	CONST_PRESENCE_EQUIPPED_SLAVE = "equipped-slave"
	CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
	CONST_PRESENCE_INACCESSIBLE = "inaccessible"
	CONST_PRESENCE_MISMATCH = "mismatch"
	CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
	CONST_PRESENCE_MISMATCH_SLAVE = "mismatch-slave"
	CONST_PRESENCE_MISSING = "missing"
	CONST_PRESENCE_MISSING_SLAVE = "missing-slave"
	CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
	CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
	CONST_PRESENCE_UNKNOWN = "unknown"
	CONST_TYPE_PHYSICAL = "physical"
	CONST_TYPE_UNKNOWN = "unknown"
	CONST_TYPE_VIRTUAL = "virtual"
