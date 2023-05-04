import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentChassisFsmStage(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentChassisFsmStage")

	@staticmethod
	def ClassId():
		return "equipmentChassisFsmStage"

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
	CONST_NAME_DYNAMIC_REALLOCATION_BEGIN = "DynamicReallocationBegin"
	CONST_NAME_DYNAMIC_REALLOCATION_CONFIG = "DynamicReallocationConfig"
	CONST_NAME_DYNAMIC_REALLOCATION_FAIL = "DynamicReallocationFail"
	CONST_NAME_DYNAMIC_REALLOCATION_SUCCESS = "DynamicReallocationSuccess"
	CONST_NAME_POWER_CAP_BEGIN = "PowerCapBegin"
	CONST_NAME_POWER_CAP_CONFIG = "PowerCapConfig"
	CONST_NAME_POWER_CAP_FAIL = "PowerCapFail"
	CONST_NAME_POWER_CAP_SUCCESS = "PowerCapSuccess"
	CONST_NAME_PSU_POLICY_CONFIG_BEGIN = "PsuPolicyConfigBegin"
	CONST_NAME_PSU_POLICY_CONFIG_EXECUTE = "PsuPolicyConfigExecute"
	CONST_NAME_PSU_POLICY_CONFIG_FAIL = "PsuPolicyConfigFail"
	CONST_NAME_PSU_POLICY_CONFIG_SUCCESS = "PsuPolicyConfigSuccess"
	CONST_NAME_REMOVE_CHASSIS_BEGIN = "RemoveChassisBegin"
	CONST_NAME_REMOVE_CHASSIS_DECOMISSION = "RemoveChassisDecomission"
	CONST_NAME_REMOVE_CHASSIS_DISABLE_END_POINT = "RemoveChassisDisableEndPoint"
	CONST_NAME_REMOVE_CHASSIS_FAIL = "RemoveChassisFail"
	CONST_NAME_REMOVE_CHASSIS_SUCCESS = "RemoveChassisSuccess"
	CONST_NAME_REMOVE_CHASSIS_UN_IDENTIFY_LOCAL = "RemoveChassisUnIdentifyLocal"
	CONST_NAME_REMOVE_CHASSIS_UN_IDENTIFY_PEER = "RemoveChassisUnIdentifyPeer"
	CONST_NAME_REMOVE_CHASSIS_WAIT = "RemoveChassisWait"
	CONST_NAME_NOP = "nop"
	CONST_STAGE_STATUS_FAIL = "fail"
	CONST_STAGE_STATUS_IN_PROGRESS = "inProgress"
	CONST_STAGE_STATUS_NOP = "nop"
	CONST_STAGE_STATUS_PENDING = "pending"
	CONST_STAGE_STATUS_SKIP = "skip"
	CONST_STAGE_STATUS_SUCCESS = "success"
	CONST_STAGE_STATUS_THROTTLED = "throttled"
