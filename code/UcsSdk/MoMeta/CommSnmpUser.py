import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommSnmpUser(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommSnmpUser")

	@staticmethod
	def ClassId():
		return "commSnmpUser"

	AUTH = "Auth"
	CONFIG_STATE = "ConfigState"
	CONFIG_STATUS_MESSAGE = "ConfigStatusMessage"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	PRIV_PWD_SET = "PrivPwdSet"
	PRIVPWD = "Privpwd"
	PWD = "Pwd"
	PWD_SET = "PwdSet"
	RN = "Rn"
	STATUS = "Status"
	USE_AES = "UseAes"

	CONST_AUTH_MD5 = "md5"
	CONST_AUTH_SHA = "sha"
	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_CONFIG_STATE_OK = "ok"
	CONST_PRIV_PWD_SET_FALSE = "false"
	CONST_PRIV_PWD_SET_NO = "no"
	CONST_PRIV_PWD_SET_TRUE = "true"
	CONST_PRIV_PWD_SET_YES = "yes"
	CONST_PWD_SET_FALSE = "false"
	CONST_PWD_SET_NO = "no"
	CONST_PWD_SET_TRUE = "true"
	CONST_PWD_SET_YES = "yes"
	CONST_USE_AES_FALSE = "false"
	CONST_USE_AES_NO = "no"
	CONST_USE_AES_TRUE = "true"
	CONST_USE_AES_YES = "yes"
