import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysdebugLogControlModule(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysdebugLogControlModule")

	@staticmethod
	def ClassId():
		return "sysdebugLogControlModule"

	DEFAULT_LEVEL = "DefaultLevel"
	DN = "Dn"
	LEVEL = "Level"
	NAME = "Name"
	RESET = "Reset"
	RN = "Rn"
	STATUS = "Status"

	CONST_DEFAULT_LEVEL_CRIT = "crit"
	CONST_DEFAULT_LEVEL_DEBUG0 = "debug0"
	CONST_DEFAULT_LEVEL_DEBUG1 = "debug1"
	CONST_DEFAULT_LEVEL_DEBUG2 = "debug2"
	CONST_DEFAULT_LEVEL_DEBUG3 = "debug3"
	CONST_DEFAULT_LEVEL_DEBUG4 = "debug4"
	CONST_DEFAULT_LEVEL_INFO = "info"
	CONST_DEFAULT_LEVEL_MAJOR = "major"
	CONST_DEFAULT_LEVEL_MINOR = "minor"
	CONST_DEFAULT_LEVEL_WARN = "warn"
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
	CONST_RESET_FALSE = "false"
	CONST_RESET_NO = "no"
	CONST_RESET_TRUE = "true"
	CONST_RESET_YES = "yes"
