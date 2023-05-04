import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtpolRegistryFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtpolRegistryFsmStage")

	@staticmethod
	def ClassId():
		return "extpolRegistryFsmStage"

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
	CONST_NAME_CROSS_DOMAIN_CONFIG_BEGIN = "crossDomainConfigBegin"
	CONST_NAME_CROSS_DOMAIN_CONFIG_FAIL = "crossDomainConfigFail"
	CONST_NAME_CROSS_DOMAIN_CONFIG_SET_LOCAL = "crossDomainConfigSetLocal"
	CONST_NAME_CROSS_DOMAIN_CONFIG_SET_PEER = "crossDomainConfigSetPeer"
	CONST_NAME_CROSS_DOMAIN_CONFIG_SUCCESS = "crossDomainConfigSuccess"
	CONST_NAME_CROSS_DOMAIN_DELETE_BEGIN = "crossDomainDeleteBegin"
	CONST_NAME_CROSS_DOMAIN_DELETE_FAIL = "crossDomainDeleteFail"
	CONST_NAME_CROSS_DOMAIN_DELETE_SET_LOCAL = "crossDomainDeleteSetLocal"
	CONST_NAME_CROSS_DOMAIN_DELETE_SET_PEER = "crossDomainDeleteSetPeer"
	CONST_NAME_CROSS_DOMAIN_DELETE_SUCCESS = "crossDomainDeleteSuccess"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
