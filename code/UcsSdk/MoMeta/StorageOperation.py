import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageOperation(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageOperation")

	@staticmethod
	def ClassId():
		return "storageOperation"

	DN = "Dn"
	END_TIME = "EndTime"
	NAME = "Name"
	OPER_STATE = "OperState"
	PROGRESS = "Progress"
	RN = "Rn"
	START_TIME = "StartTime"
	STATUS = "Status"
	STATUS_DESCR = "StatusDescr"

	CONST_END_TIME_N_A = "N/A"
	CONST_NAME_CONSISTENCY_CHECK = "consistency-check"
	CONST_NAME_INITIALIZATION = "initialization"
	CONST_NAME_PATROL_READ = "patrol-read"
	CONST_NAME_REBUILD = "rebuild"
	CONST_NAME_RECONSTRUCTION = "reconstruction"
	CONST_NAME_RELEARNING = "relearning"
	CONST_OPER_STATE_COMPLETED = "completed"
	CONST_OPER_STATE_FAILED = "failed"
	CONST_OPER_STATE_IN_PROGRESS = "in-progress"
	CONST_OPER_STATE_UNKNOWN = "unknown"
	CONST_PROGRESS_UNKNOWN = "unknown"
	CONST_START_TIME_N_A = "N/A"
