import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareCatalogPack(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareCatalogPack")

	@staticmethod
	def ClassId():
		return "firmwareCatalogPack"

	CATALOG_NAME = "CatalogName"
	CATALOG_VERSION = "CatalogVersion"
	CONFIG_STATE = "ConfigState"
	CONFIG_STATUS_MESSAGE = "ConfigStatusMessage"
	DESCR = "Descr"
	DN = "Dn"
	MODE = "Mode"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STAGE_SIZE = "StageSize"
	STATUS = "Status"
	UPDATE_TRIGGER = "UpdateTrigger"

	CONST_CONFIG_STATE_FAILED = "failed"
	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_CONFIG_STATE_OK = "ok"
	CONST_INT_ID_NONE = "none"
	CONST_MODE_ONE_SHOT = "one-shot"
	CONST_MODE_STAGED = "staged"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_UPDATE_TRIGGER_IMMEDIATE = "immediate"
