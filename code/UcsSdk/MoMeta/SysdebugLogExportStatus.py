import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysdebugLogExportStatus(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysdebugLogExportStatus")

	@staticmethod
	def ClassId():
		return "sysdebugLogExportStatus"

	DN = "Dn"
	EXPORT_FAILURE_REASON = "ExportFailureReason"
	EXPORT_STATUS = "ExportStatus"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"

	CONST_EXPORT_STATUS_FAILURE = "failure"
	CONST_EXPORT_STATUS_SUCCESS = "success"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
