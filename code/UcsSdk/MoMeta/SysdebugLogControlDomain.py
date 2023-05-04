import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysdebugLogControlDomain(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysdebugLogControlDomain")

	@staticmethod
	def ClassId():
		return "sysdebugLogControlDomain"

	DN = "Dn"
	LEVEL = "Level"
	LEVEL_FLAG = "LevelFlag"
	NAME = "Name"
	PERSIST = "Persist"
	RESET = "Reset"
	RN = "Rn"
	STATUS = "Status"

	CONST_LEVEL_CRIT = "crit"
	CONST_LEVEL_DEBUG0 = "debug0"
	CONST_LEVEL_DEBUG1 = "debug1"
	CONST_LEVEL_DEBUG2 = "debug2"
	CONST_LEVEL_DEBUG3 = "debug3"
	CONST_LEVEL_DEBUG4 = "debug4"
	CONST_LEVEL_INFO = "info"
	CONST_LEVEL_MAJOR = "major"
	CONST_LEVEL_MINOR = "minor"
	CONST_LEVEL_WARN = "warn"
	CONST_LEVEL_FLAG_FALSE = "false"
	CONST_LEVEL_FLAG_NO = "no"
	CONST_LEVEL_FLAG_TRUE = "true"
	CONST_LEVEL_FLAG_YES = "yes"
	CONST_NAME_SYSMGMT = "sysmgmt"
	CONST_PERSIST_FALSE = "false"
	CONST_PERSIST_NO = "no"
	CONST_PERSIST_TRUE = "true"
	CONST_PERSIST_YES = "yes"
	CONST_RESET_FALSE = "false"
	CONST_RESET_NO = "no"
	CONST_RESET_TRUE = "true"
	CONST_RESET_YES = "yes"
