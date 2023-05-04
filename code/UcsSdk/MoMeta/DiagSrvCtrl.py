import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DiagSrvCtrl(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DiagSrvCtrl")

	@staticmethod
	def ClassId():
		return "diagSrvCtrl"

	ADMIN_STATE = "AdminState"
	DN = "Dn"
	END_TS = "EndTs"
	END_TS_M = "EndTsM"
	ERROR_DESCR = "ErrorDescr"
	IMG_LOC = "ImgLoc"
	IMG_NAME = "ImgName"
	OPER_QUALIFIER = "OperQualifier"
	OPER_STATE = "OperState"
	RN = "Rn"
	RUN_POLICY_NAME = "RunPolicyName"
	START_TS = "StartTs"
	START_TS_M = "StartTsM"
	STATUS = "Status"
	TYPE = "Type"

	CONST_ADMIN_STATE_CANCEL = "cancel"
	CONST_ADMIN_STATE_READY = "ready"
	CONST_ADMIN_STATE_TRIGGER = "trigger"
	CONST_END_TS_NEVER = "never"
	CONST_END_TS_M_NEVER = "never"
	CONST_OPER_STATE_CANCELLED = "cancelled"
	CONST_OPER_STATE_COMPLETE = "complete"
	CONST_OPER_STATE_FAILED = "failed"
	CONST_OPER_STATE_IN_PROGRESS = "in-progress"
	CONST_OPER_STATE_NOT_RUN = "not-run"
	CONST_OPER_STATE_SCHEDULED = "scheduled"
	CONST_START_TS_NEVER = "never"
	CONST_START_TS_M_NEVER = "never"
	CONST_TYPE_EFI = "EFI"
	CONST_TYPE_FULL = "full"
