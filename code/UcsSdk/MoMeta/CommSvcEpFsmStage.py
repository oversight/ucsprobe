import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommSvcEpFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommSvcEpFsmStage")

	@staticmethod
	def ClassId():
		return "commSvcEpFsmStage"

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
	CONST_NAME_NOP = "nop"
	CONST_NAME_RESTART_WEB_SVC_BEGIN = "restartWebSvcBegin"
	CONST_NAME_RESTART_WEB_SVC_FAIL = "restartWebSvcFail"
	CONST_NAME_RESTART_WEB_SVC_LOCAL = "restartWebSvcLocal"
	CONST_NAME_RESTART_WEB_SVC_PEER = "restartWebSvcPeer"
	CONST_NAME_RESTART_WEB_SVC_SUCCESS = "restartWebSvcSuccess"
	CONST_NAME_UPDATE_SVC_EP_BEGIN = "updateSvcEpBegin"
	CONST_NAME_UPDATE_SVC_EP_FAIL = "updateSvcEpFail"
	CONST_NAME_UPDATE_SVC_EP_PROPOGATE_EP_SETTINGS = "updateSvcEpPropogateEpSettings"
	CONST_NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_LOCAL = "updateSvcEpPropogateEpTimeZoneSettingsLocal"
	CONST_NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_PEER = "updateSvcEpPropogateEpTimeZoneSettingsPeer"
	CONST_NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_TO_ADAPTORS_LOCAL = "updateSvcEpPropogateEpTimeZoneSettingsToAdaptorsLocal"
	CONST_NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_TO_ADAPTORS_PEER = "updateSvcEpPropogateEpTimeZoneSettingsToAdaptorsPeer"
	CONST_NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_TO_FEX_IOM_LOCAL = "updateSvcEpPropogateEpTimeZoneSettingsToFexIomLocal"
	CONST_NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_TO_FEX_IOM_PEER = "updateSvcEpPropogateEpTimeZoneSettingsToFexIomPeer"
	CONST_NAME_UPDATE_SVC_EP_SET_EP_LOCAL = "updateSvcEpSetEpLocal"
	CONST_NAME_UPDATE_SVC_EP_SET_EP_PEER = "updateSvcEpSetEpPeer"
	CONST_NAME_UPDATE_SVC_EP_SUCCESS = "updateSvcEpSuccess"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
