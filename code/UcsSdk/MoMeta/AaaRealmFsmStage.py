import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaRealmFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaRealmFsmStage")

	@staticmethod
	def ClassId():
		return "aaaRealmFsmStage"

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
	CONST_NAME_UPDATE_REALM_BEGIN = "updateRealmBegin"
	CONST_NAME_UPDATE_REALM_FAIL = "updateRealmFail"
	CONST_NAME_UPDATE_REALM_SET_REALM_LOCAL = "updateRealmSetRealmLocal"
	CONST_NAME_UPDATE_REALM_SET_REALM_PEER = "updateRealmSetRealmPeer"
	CONST_NAME_UPDATE_REALM_SUCCESS = "updateRealmSuccess"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
