import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtPmonEntry(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtPmonEntry")

	@staticmethod
	def ClassId():
		return "mgmtPmonEntry"

	DN = "Dn"
	EXIT_SIGNAL = "ExitSignal"
	FULL_PATHNAME = "FullPathname"
	HEAP_SIZE = "HeapSize"
	HEAP_SIZE16_GB = "HeapSize16Gb"
	LAST_EXIT_CODE = "LastExitCode"
	MAX_RETRIES = "MaxRetries"
	NAME = "Name"
	RETRIES = "Retries"
	RN = "Rn"
	SPURIOUS_RETRIES = "SpuriousRetries"
	STATE = "State"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	WORKING_DIRECTORY = "WorkingDirectory"

	CONST_STATE_ERROR = "error"
	CONST_STATE_EXIT_PENDING = "exit_pending"
	CONST_STATE_FAILED = "failed"
	CONST_STATE_IDLE = "idle"
	CONST_STATE_KILLED = "killed"
	CONST_STATE_PENDING = "pending"
	CONST_STATE_RUNNING = "running"
	CONST_STATE_TERMINATED = "terminated"
	CONST_STATE_UNKNOWN = "unknown"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
