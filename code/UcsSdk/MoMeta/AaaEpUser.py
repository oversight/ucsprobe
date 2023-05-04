import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaEpUser(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaEpUser")

	@staticmethod
	def ClassId():
		return "aaaEpUser"

	CONFIG_STATE = "ConfigState"
	CONFIG_STATUS_MESSAGE = "ConfigStatusMessage"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	PRIV = "Priv"
	PWD = "Pwd"
	PWD_SET = "PwdSet"
	RN = "Rn"
	STATUS = "Status"

	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_CONFIG_STATE_OK = "ok"
	CONST_PRIV_ADMIN = "admin"
	CONST_PRIV_READONLY = "readonly"
	CONST_PWD_SET_FALSE = "false"
	CONST_PWD_SET_NO = "no"
	CONST_PWD_SET_TRUE = "true"
	CONST_PWD_SET_YES = "yes"
