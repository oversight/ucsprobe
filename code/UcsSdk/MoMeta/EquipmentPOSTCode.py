import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPOSTCode(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPOSTCode")

	@staticmethod
	def ClassId():
		return "equipmentPOSTCode"

	CODE = "Code"
	DESCR = "Descr"
	DN = "Dn"
	GLOBAL_ID = "GlobalId"
	LOCAL_ID = "LocalId"
	METHOD = "Method"
	NAME = "Name"
	RECOVERABLE = "Recoverable"
	RECOVERY_ACTION = "RecoveryAction"
	RN = "Rn"
	SEVERITY = "Severity"
	STATUS = "Status"

	CONST_GLOBAL_ID_NO_ERRORS = "No Errors"
	CONST_LOCAL_ID_NO_ERRORS = "No Errors"
	CONST_RECOVERABLE_NON_RECOVERABLE = "non-recoverable"
	CONST_RECOVERABLE_RECOVERABLE = "recoverable"
	CONST_RECOVERABLE_UNKNOWN = "unknown"
	CONST_SEVERITY_CLEARED = "cleared"
	CONST_SEVERITY_CONDITION = "condition"
	CONST_SEVERITY_CRITICAL = "critical"
	CONST_SEVERITY_INFO = "info"
	CONST_SEVERITY_MAJOR = "major"
	CONST_SEVERITY_MINOR = "minor"
	CONST_SEVERITY_WARNING = "warning"
