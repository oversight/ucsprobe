import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentFexFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentFexFsmStage")

	@staticmethod
	def ClassId():
		return "equipmentFexFsmStage"

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
	CONST_NAME_REMOVE_FEX_BEGIN = "RemoveFexBegin"
	CONST_NAME_REMOVE_FEX_CLEANUP_ENTRIES = "RemoveFexCleanupEntries"
	CONST_NAME_REMOVE_FEX_DECOMISSION = "RemoveFexDecomission"
	CONST_NAME_REMOVE_FEX_FAIL = "RemoveFexFail"
	CONST_NAME_REMOVE_FEX_SUCCESS = "RemoveFexSuccess"
	CONST_NAME_REMOVE_FEX_UN_IDENTIFY_LOCAL = "RemoveFexUnIdentifyLocal"
	CONST_NAME_REMOVE_FEX_WAIT = "RemoveFexWait"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
