import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareUpgradeDetail(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareUpgradeDetail")

	@staticmethod
	def ClassId():
		return "firmwareUpgradeDetail"

	CATEGORY = "Category"
	DESCRIPTION = "Description"
	DN = "Dn"
	ID = "Id"
	RN = "Rn"
	SEVERITY = "Severity"
	STATUS = "Status"

	CONST_CATEGORY_CATALOG = "catalog"
	CONST_CATEGORY_CONFIG = "config"
	CONST_CATEGORY_DATA_LOAD = "data-load"
	CONST_CATEGORY_FAULTS = "faults"
	CONST_CATEGORY_OTHER = "other"
	CONST_CATEGORY_SERVER_REBOOT = "server-reboot"
	CONST_SEVERITY_ERROR = "error"
	CONST_SEVERITY_FATAL = "fatal"
	CONST_SEVERITY_INFO = "info"
	CONST_SEVERITY_UNKNOWN = "unknown"
	CONST_SEVERITY_WARN = "warn"
