import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareUpgradeInfo(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareUpgradeInfo")

	@staticmethod
	def ClassId():
		return "firmwareUpgradeInfo"

	DN = "Dn"
	MESSAGE = "Message"
	RN = "Rn"
	STATUS = "Status"
	TIME_STAMP = "TimeStamp"
	VALIDATE_STATUS = "ValidateStatus"
	VERSION = "Version"

	CONST_TIME_STAMP_NEVER = "never"
	CONST_VALIDATE_STATUS_FAILED = "failed"
	CONST_VALIDATE_STATUS_IN_PROGRESS = "in-progress"
	CONST_VALIDATE_STATUS_SKIPPED = "skipped"
	CONST_VALIDATE_STATUS_SUCCESS = "success"
	CONST_VALIDATE_STATUS_UNKNOWN = "unknown"
	CONST_VALIDATE_STATUS_WARNINGS = "warnings"
