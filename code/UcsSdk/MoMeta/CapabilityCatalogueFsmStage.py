import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CapabilityCatalogueFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CapabilityCatalogueFsmStage")

	@staticmethod
	def ClassId():
		return "capabilityCatalogueFsmStage"

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
	CONST_NAME_ACTIVATE_CATALOG_APPLY_CATALOG = "ActivateCatalogApplyCatalog"
	CONST_NAME_ACTIVATE_CATALOG_BEGIN = "ActivateCatalogBegin"
	CONST_NAME_ACTIVATE_CATALOG_COPY_CAT_FROM_REP = "ActivateCatalogCopyCatFromRep"
	CONST_NAME_ACTIVATE_CATALOG_COPY_EXTERNAL_REP_TO_REMOTE = "ActivateCatalogCopyExternalRepToRemote"
	CONST_NAME_ACTIVATE_CATALOG_COPY_REMOTE = "ActivateCatalogCopyRemote"
	CONST_NAME_ACTIVATE_CATALOG_EVALUATE_STATUS = "ActivateCatalogEvaluateStatus"
	CONST_NAME_ACTIVATE_CATALOG_FAIL = "ActivateCatalogFail"
	CONST_NAME_ACTIVATE_CATALOG_RESCAN_IMAGES = "ActivateCatalogRescanImages"
	CONST_NAME_ACTIVATE_CATALOG_SUCCESS = "ActivateCatalogSuccess"
	CONST_NAME_ACTIVATE_CATALOG_UNPACK_LOCAL = "ActivateCatalogUnpackLocal"
	CONST_NAME_DEPLOY_CATALOGUE_BEGIN = "DeployCatalogueBegin"
	CONST_NAME_DEPLOY_CATALOGUE_FAIL = "DeployCatalogueFail"
	CONST_NAME_DEPLOY_CATALOGUE_FINALIZE = "DeployCatalogueFinalize"
	CONST_NAME_DEPLOY_CATALOGUE_SUCCESS = "DeployCatalogueSuccess"
	CONST_NAME_DEPLOY_CATALOGUE_SYNC_BLADE_AGLOCAL = "DeployCatalogueSyncBladeAGLocal"
	CONST_NAME_DEPLOY_CATALOGUE_SYNC_BLADE_AGREMOTE = "DeployCatalogueSyncBladeAGRemote"
	CONST_NAME_DEPLOY_CATALOGUE_SYNC_HOSTAGENT_AGLOCAL = "DeployCatalogueSyncHostagentAGLocal"
	CONST_NAME_DEPLOY_CATALOGUE_SYNC_HOSTAGENT_AGREMOTE = "DeployCatalogueSyncHostagentAGRemote"
	CONST_NAME_DEPLOY_CATALOGUE_SYNC_NIC_AGLOCAL = "DeployCatalogueSyncNicAGLocal"
	CONST_NAME_DEPLOY_CATALOGUE_SYNC_NIC_AGREMOTE = "DeployCatalogueSyncNicAGRemote"
	CONST_NAME_DEPLOY_CATALOGUE_SYNC_PORT_AGLOCAL = "DeployCatalogueSyncPortAGLocal"
	CONST_NAME_DEPLOY_CATALOGUE_SYNC_PORT_AGREMOTE = "DeployCatalogueSyncPortAGRemote"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
