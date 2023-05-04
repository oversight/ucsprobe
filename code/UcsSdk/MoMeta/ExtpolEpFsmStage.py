import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtpolEpFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtpolEpFsmStage")

	@staticmethod
	def ClassId():
		return "extpolEpFsmStage"

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
	CONST_NAME_REGISTER_FSM_BEGIN = "RegisterFsmBegin"
	CONST_NAME_REGISTER_FSM_EXECUTE = "RegisterFsmExecute"
	CONST_NAME_REGISTER_FSM_FAIL = "RegisterFsmFail"
	CONST_NAME_REGISTER_FSM_SUCCESS = "RegisterFsmSuccess"
	CONST_NAME_NOP = "nop"
	CONST_NAME_REPAIR_CERT_BEGIN = "repairCertBegin"
	CONST_NAME_REPAIR_CERT_CLEAN_OLD_DATA = "repairCertCleanOldData"
	CONST_NAME_REPAIR_CERT_FAIL = "repairCertFail"
	CONST_NAME_REPAIR_CERT_REQUEST = "repairCertRequest"
	CONST_NAME_REPAIR_CERT_SUCCESS = "repairCertSuccess"
	CONST_NAME_REPAIR_CERT_UNREGISTER = "repairCertUnregister"
	CONST_NAME_REPAIR_CERT_VERIFY = "repairCertVerify"
	CONST_NAME_REPAIR_CERT_VERIFY_GUID = "repairCertVerifyGuid"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
