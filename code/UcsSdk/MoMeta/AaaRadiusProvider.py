import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaRadiusProvider(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaRadiusProvider")

	@staticmethod
	def ClassId():
		return "aaaRadiusProvider"

	AUTH_PORT = "AuthPort"
	DESCR = "Descr"
	DN = "Dn"
	ENC_KEY = "EncKey"
	KEY = "Key"
	KEY_SET = "KeySet"
	NAME = "Name"
	ORDER = "Order"
	RETRIES = "Retries"
	RN = "Rn"
	SERVICE = "Service"
	STATUS = "Status"
	TIMEOUT = "Timeout"

	CONST_KEY_SET_FALSE = "false"
	CONST_KEY_SET_NO = "no"
	CONST_KEY_SET_TRUE = "true"
	CONST_KEY_SET_YES = "yes"
	CONST_ORDER_LOWEST_AVAILABLE = "lowest-available"
	CONST_SERVICE_ACCOUNTING = "accounting"
	CONST_SERVICE_ALL = "all"
	CONST_SERVICE_AUTHORIZATION = "authorization"
