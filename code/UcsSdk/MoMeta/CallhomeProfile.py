import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CallhomeProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CallhomeProfile")

	@staticmethod
	def ClassId():
		return "callhomeProfile"

	ALERT_GROUPS = "AlertGroups"
	DESCR = "Descr"
	DN = "Dn"
	FORMAT = "Format"
	LEVEL = "Level"
	MAX_SIZE = "MaxSize"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

	CONST_FORMAT_FULL_TXT = "fullTxt"
	CONST_FORMAT_SHORT_TXT = "shortTxt"
	CONST_FORMAT_XML = "xml"
	CONST_LEVEL_CRITICAL = "critical"
	CONST_LEVEL_DEBUG = "debug"
	CONST_LEVEL_DISASTER = "disaster"
	CONST_LEVEL_FATAL = "fatal"
	CONST_LEVEL_MAJOR = "major"
	CONST_LEVEL_MINOR = "minor"
	CONST_LEVEL_NORMAL = "normal"
	CONST_LEVEL_NOTIFICATION = "notification"
	CONST_LEVEL_WARNING = "warning"
