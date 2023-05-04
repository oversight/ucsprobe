import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareSystemFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareSystemFsmStage")

	@staticmethod
	def ClassId():
		return "firmwareSystemFsmStage"

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
	CONST_NAME_APPLY_CATALOG_PACK_ACTIVATE_CATALOG = "ApplyCatalogPackActivateCatalog"
	CONST_NAME_APPLY_CATALOG_PACK_BEGIN = "ApplyCatalogPackBegin"
	CONST_NAME_APPLY_CATALOG_PACK_FAIL = "ApplyCatalogPackFail"
	CONST_NAME_APPLY_CATALOG_PACK_RESOLVE_DISTRIBUTABLE = "ApplyCatalogPackResolveDistributable"
	CONST_NAME_APPLY_CATALOG_PACK_RESOLVE_DISTRIBUTABLE_NAMES = "ApplyCatalogPackResolveDistributableNames"
	CONST_NAME_APPLY_CATALOG_PACK_RESOLVE_IMAGES = "ApplyCatalogPackResolveImages"
	CONST_NAME_APPLY_CATALOG_PACK_SUCCESS = "ApplyCatalogPackSuccess"
	CONST_NAME_DEPLOY_ACTIVATE_IOM = "DeployActivateIOM"
	CONST_NAME_DEPLOY_ACTIVATE_LOCAL_FI = "DeployActivateLocalFI"
	CONST_NAME_DEPLOY_ACTIVATE_REMOTE_FI = "DeployActivateRemoteFI"
	CONST_NAME_DEPLOY_ACTIVATE_UCSM = "DeployActivateUCSM"
	CONST_NAME_DEPLOY_BEGIN = "DeployBegin"
	CONST_NAME_DEPLOY_FAIL = "DeployFail"
	CONST_NAME_DEPLOY_POLL_ACTIVATE_OF_IOM = "DeployPollActivateOfIOM"
	CONST_NAME_DEPLOY_POLL_ACTIVATE_OF_LOCAL_FI = "DeployPollActivateOfLocalFI"
	CONST_NAME_DEPLOY_POLL_ACTIVATE_OF_REMOTE_FI = "DeployPollActivateOfRemoteFI"
	CONST_NAME_DEPLOY_POLL_ACTIVATE_OF_UCSM = "DeployPollActivateOfUCSM"
	CONST_NAME_DEPLOY_POLL_UPDATE_OF_IOM = "DeployPollUpdateOfIOM"
	CONST_NAME_DEPLOY_RESOLVE_DISTRIBUTABLE = "DeployResolveDistributable"
	CONST_NAME_DEPLOY_RESOLVE_DISTRIBUTABLE_NAMES = "DeployResolveDistributableNames"
	CONST_NAME_DEPLOY_RESOLVE_IMAGES = "DeployResolveImages"
	CONST_NAME_DEPLOY_SUCCESS = "DeploySuccess"
	CONST_NAME_DEPLOY_UPDATE_IOM = "DeployUpdateIOM"
	CONST_NAME_DEPLOY_WAIT_FOR_DEPLOY = "DeployWaitForDeploy"
	CONST_NAME_DEPLOY_WAIT_FOR_USER_ACK = "DeployWaitForUserAck"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
