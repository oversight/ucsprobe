import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EventEpCtrl(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EventEpCtrl")

	@staticmethod
	def ClassId():
		return "eventEpCtrl"

	DN = "Dn"
	LEVEL = "Level"
	REVERT_TIMEOUT = "RevertTimeout"
	RN = "Rn"
	STATUS = "Status"

	CONST_LEVEL_CLEARED = "cleared"
	CONST_LEVEL_CONDITION = "condition"
	CONST_LEVEL_CRITICAL = "critical"
	CONST_LEVEL_INFO = "info"
	CONST_LEVEL_MAJOR = "major"
	CONST_LEVEL_MINOR = "minor"
	CONST_LEVEL_WARNING = "warning"
	CONST_REVERT_TIMEOUT_FOREVER = "forever"
