import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CallhomeTestAlert(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CallhomeTestAlert")

	@staticmethod
	def ClassId():
		return "callhomeTestAlert"

	DESCRIPTION = "Description"
	DN = "Dn"
	GROUP = "Group"
	LEVEL = "Level"
	MESSAGE_SUBTYPE = "MessageSubtype"
	MESSAGE_TYPE = "MessageType"
	RN = "Rn"
	SEND_NOW = "SendNow"
	STATUS = "Status"

	CONST_GROUP_DIAGNOSTIC = "diagnostic"
	CONST_GROUP_ENVIRONMENTAL = "environmental"
	CONST_GROUP_UNKNOWN = "unknown"
	CONST_LEVEL_CRITICAL = "critical"
	CONST_LEVEL_DEBUG = "debug"
	CONST_LEVEL_FATAL = "fatal"
	CONST_LEVEL_MAJOR = "major"
	CONST_LEVEL_MINOR = "minor"
	CONST_LEVEL_NORMAL = "normal"
	CONST_LEVEL_NOTIFY = "notify"
	CONST_LEVEL_UNKNOWN = "unknown"
	CONST_LEVEL_WARNING = "warning"
	CONST_MESSAGE_SUBTYPE_DELTA = "delta"
	CONST_MESSAGE_SUBTYPE_FULL = "full"
	CONST_MESSAGE_SUBTYPE_GOLDMAJOR = "goldmajor"
	CONST_MESSAGE_SUBTYPE_GOLDMINOR = "goldminor"
	CONST_MESSAGE_SUBTYPE_GOLDNORMAL = "goldnormal"
	CONST_MESSAGE_SUBTYPE_MAJOR = "major"
	CONST_MESSAGE_SUBTYPE_MINOR = "minor"
	CONST_MESSAGE_SUBTYPE_NOSUBTYPE = "nosubtype"
	CONST_MESSAGE_SUBTYPE_TEST = "test"
	CONST_MESSAGE_SUBTYPE_UNKNOWN = "unknown"
	CONST_MESSAGE_TYPE_CONF = "conf"
	CONST_MESSAGE_TYPE_DIAG = "diag"
	CONST_MESSAGE_TYPE_ENV = "env"
	CONST_MESSAGE_TYPE_INVENTORY = "inventory"
	CONST_MESSAGE_TYPE_SYSLOG = "syslog"
	CONST_MESSAGE_TYPE_TEST = "test"
	CONST_MESSAGE_TYPE_UNKNOWN = "unknown"
	CONST_SEND_NOW_FALSE = "false"
	CONST_SEND_NOW_NO = "no"
	CONST_SEND_NOW_TRUE = "true"
	CONST_SEND_NOW_YES = "yes"
