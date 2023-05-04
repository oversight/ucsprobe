import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaRemoteUser(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaRemoteUser")

	@staticmethod
	def ClassId():
		return "aaaRemoteUser"

	CONFIG_STATE = "ConfigState"
	CONFIG_STATUS_MESSAGE = "ConfigStatusMessage"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	PWD = "Pwd"
	PWD_SET = "PwdSet"
	RN = "Rn"
	STATUS = "Status"

	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_CONFIG_STATE_OK = "ok"
	CONST_PWD_SET_FALSE = "false"
	CONST_PWD_SET_NO = "no"
	CONST_PWD_SET_TRUE = "true"
	CONST_PWD_SET_YES = "yes"
