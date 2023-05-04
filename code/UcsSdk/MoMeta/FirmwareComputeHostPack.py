import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareComputeHostPack(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareComputeHostPack")

	@staticmethod
	def ClassId():
		return "firmwareComputeHostPack"

	BLADE_BUNDLE_NAME = "BladeBundleName"
	BLADE_BUNDLE_VERSION = "BladeBundleVersion"
	CONFIG_QUALIFIER = "ConfigQualifier"
	DESCR = "Descr"
	DN = "Dn"
	IGNORE_COMP_CHECK = "IgnoreCompCheck"
	MODE = "Mode"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RACK_BUNDLE_NAME = "RackBundleName"
	RACK_BUNDLE_VERSION = "RackBundleVersion"
	RN = "Rn"
	STAGE_SIZE = "StageSize"
	STATUS = "Status"
	UPDATE_TRIGGER = "UpdateTrigger"

	CONST_IGNORE_COMP_CHECK_FALSE = "false"
	CONST_IGNORE_COMP_CHECK_NO = "no"
	CONST_IGNORE_COMP_CHECK_TRUE = "true"
	CONST_IGNORE_COMP_CHECK_YES = "yes"
	CONST_INT_ID_NONE = "none"
	CONST_MODE_ONE_SHOT = "one-shot"
	CONST_MODE_STAGED = "staged"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_UPDATE_TRIGGER_IMMEDIATE = "immediate"
