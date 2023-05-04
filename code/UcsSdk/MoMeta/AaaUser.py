import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaUser(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaUser")

	@staticmethod
	def ClassId():
		return "aaaUser"

	ACCOUNT_STATUS = "AccountStatus"
	CLEAR_PWD_HISTORY = "ClearPwdHistory"
	CONFIG_STATE = "ConfigState"
	CONFIG_STATUS_MESSAGE = "ConfigStatusMessage"
	DESCR = "Descr"
	DN = "Dn"
	EMAIL = "Email"
	ENC_PWD = "EncPwd"
	ENC_PWD_SET = "EncPwdSet"
	EXPIRATION = "Expiration"
	EXPIRES = "Expires"
	FIRST_NAME = "FirstName"
	LAST_NAME = "LastName"
	NAME = "Name"
	PHONE = "Phone"
	PRIV = "Priv"
	PWD = "Pwd"
	PWD_LIFE_TIME = "PwdLifeTime"
	PWD_SET = "PwdSet"
	RN = "Rn"
	STATUS = "Status"

	CONST_ACCOUNT_STATUS_ACTIVE = "active"
	CONST_ACCOUNT_STATUS_INACTIVE = "inactive"
	CONST_CLEAR_PWD_HISTORY_NO = "no"
	CONST_CLEAR_PWD_HISTORY_YES = "yes"
	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_CONFIG_STATE_OK = "ok"
	CONST_ENC_PWD_SET_FALSE = "false"
	CONST_ENC_PWD_SET_NO = "no"
	CONST_ENC_PWD_SET_TRUE = "true"
	CONST_ENC_PWD_SET_YES = "yes"
	CONST_EXPIRATION_NEVER = "never"
	CONST_EXPIRES_FALSE = "false"
	CONST_EXPIRES_NO = "no"
	CONST_EXPIRES_TRUE = "true"
	CONST_EXPIRES_YES = "yes"
	CONST_PWD_LIFE_TIME_NO_PASSWORD_EXPIRE = "no-password-expire"
	CONST_PWD_SET_FALSE = "false"
	CONST_PWD_SET_NO = "no"
	CONST_PWD_SET_TRUE = "true"
	CONST_PWD_SET_YES = "yes"
