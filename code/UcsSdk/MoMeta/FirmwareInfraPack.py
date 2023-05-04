import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareInfraPack(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareInfraPack")

	@staticmethod
	def ClassId():
		return "firmwareInfraPack"

	DESCR = "Descr"
	DN = "Dn"
	FORCE_DEPLOY = "ForceDeploy"
	INFRA_BUNDLE_NAME = "InfraBundleName"
	INFRA_BUNDLE_VERSION = "InfraBundleVersion"
	MODE = "Mode"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STAGE_SIZE = "StageSize"
	STATUS = "Status"
	UPDATE_TRIGGER = "UpdateTrigger"

	CONST_FORCE_DEPLOY_FALSE = "false"
	CONST_FORCE_DEPLOY_NO = "no"
	CONST_FORCE_DEPLOY_TRUE = "true"
	CONST_FORCE_DEPLOY_YES = "yes"
	CONST_INT_ID_NONE = "none"
	CONST_MODE_ONE_SHOT = "one-shot"
	CONST_MODE_STAGED = "staged"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_UPDATE_TRIGGER_IMMEDIATE = "immediate"
