import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PkiEpFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PkiEpFsmStage")

	@staticmethod
	def ClassId():
		return "pkiEpFsmStage"

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
	CONST_NAME_UPDATE_EP_BEGIN = "updateEpBegin"
	CONST_NAME_UPDATE_EP_FAIL = "updateEpFail"
	CONST_NAME_UPDATE_EP_POST_SET_KEY_RING_LOCAL = "updateEpPostSetKeyRingLocal"
	CONST_NAME_UPDATE_EP_POST_SET_KEY_RING_PEER = "updateEpPostSetKeyRingPeer"
	CONST_NAME_UPDATE_EP_SET_KEY_RING_LOCAL = "updateEpSetKeyRingLocal"
	CONST_NAME_UPDATE_EP_SET_KEY_RING_PEER = "updateEpSetKeyRingPeer"
	CONST_NAME_UPDATE_EP_SUCCESS = "updateEpSuccess"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
