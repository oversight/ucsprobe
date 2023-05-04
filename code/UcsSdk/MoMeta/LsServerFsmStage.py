import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsServerFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsServerFsmStage")

	@staticmethod
	def ClassId():
		return "lsServerFsmStage"

	DESCR = "Descr"
	DN = "Dn"
	LAST_UPDATE_TIME = "LastUpdateTime"
	NAME = "Name"
	ORDER = "Order"
	RETRY = "Retry"
	RN = "Rn"
	STAGE_STATUS = "StageStatus"
	STATUS = "Status"

	CONST_LAST_UPDATE_TIME_ = ""
	CONST_NAME_CONFIGURE_ANALYZE_IMPACT = "ConfigureAnalyzeImpact"
	CONST_NAME_CONFIGURE_APPLY_CONFIG = "ConfigureApplyConfig"
	CONST_NAME_CONFIGURE_APPLY_DEFAULT_IDENTIFIERS = "ConfigureApplyDefaultIdentifiers"
	CONST_NAME_CONFIGURE_APPLY_IDENTIFIERS = "ConfigureApplyIdentifiers"
	CONST_NAME_CONFIGURE_APPLY_POLICIES = "ConfigureApplyPolicies"
	CONST_NAME_CONFIGURE_APPLY_TEMPLATE = "ConfigureApplyTemplate"
	CONST_NAME_CONFIGURE_BEGIN = "ConfigureBegin"
	CONST_NAME_CONFIGURE_COMMIT_STORAGE = "ConfigureCommitStorage"
	CONST_NAME_CONFIGURE_EVALUATE_ASSOCIATION = "ConfigureEvaluateAssociation"
	CONST_NAME_CONFIGURE_FAIL = "ConfigureFail"
	CONST_NAME_CONFIGURE_PROVISION_STORAGE = "ConfigureProvisionStorage"
	CONST_NAME_CONFIGURE_RESOLVE_BOOT_CONFIG = "ConfigureResolveBootConfig"
	CONST_NAME_CONFIGURE_RESOLVE_DEFAULT_IDENTIFIERS = "ConfigureResolveDefaultIdentifiers"
	CONST_NAME_CONFIGURE_RESOLVE_DISTRIBUTABLE = "ConfigureResolveDistributable"
	CONST_NAME_CONFIGURE_RESOLVE_DISTRIBUTABLE_NAMES = "ConfigureResolveDistributableNames"
	CONST_NAME_CONFIGURE_RESOLVE_IDENTIFIERS = "ConfigureResolveIdentifiers"
	CONST_NAME_CONFIGURE_RESOLVE_IMAGES = "ConfigureResolveImages"
	CONST_NAME_CONFIGURE_RESOLVE_NETWORK_POLICIES = "ConfigureResolveNetworkPolicies"
	CONST_NAME_CONFIGURE_RESOLVE_NETWORK_TEMPLATES = "ConfigureResolveNetworkTemplates"
	CONST_NAME_CONFIGURE_RESOLVE_POLICIES = "ConfigureResolvePolicies"
	CONST_NAME_CONFIGURE_RESOLVE_SCHEDULE = "ConfigureResolveSchedule"
	CONST_NAME_CONFIGURE_SUCCESS = "ConfigureSuccess"
	CONST_NAME_CONFIGURE_VALIDATE_POLICY_OWNERSHIP = "ConfigureValidatePolicyOwnership"
	CONST_NAME_CONFIGURE_WAIT_FOR_ASSOC_COMPLETION = "ConfigureWaitForAssocCompletion"
	CONST_NAME_CONFIGURE_WAIT_FOR_COMMIT_STORAGE = "ConfigureWaitForCommitStorage"
	CONST_NAME_CONFIGURE_WAIT_FOR_MAINT_PERMISSION = "ConfigureWaitForMaintPermission"
	CONST_NAME_CONFIGURE_WAIT_FOR_MAINT_WINDOW = "ConfigureWaitForMaintWindow"
	CONST_NAME_CONFIGURE_WAIT_FOR_STORAGE_PROVISION = "ConfigureWaitForStorageProvision"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
