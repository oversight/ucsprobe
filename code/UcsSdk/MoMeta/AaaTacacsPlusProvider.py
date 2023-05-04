import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaTacacsPlusProvider(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaTacacsPlusProvider")

	@staticmethod
	def ClassId():
		return "aaaTacacsPlusProvider"

	DESCR = "Descr"
	DN = "Dn"
	ENC_KEY = "EncKey"
	KEY = "Key"
	KEY_SET = "KeySet"
	NAME = "Name"
	ORDER = "Order"
	PORT = "Port"
	RETRIES = "Retries"
	RN = "Rn"
	STATUS = "Status"
	TIMEOUT = "Timeout"

	CONST_KEY_SET_FALSE = "false"
	CONST_KEY_SET_NO = "no"
	CONST_KEY_SET_TRUE = "true"
	CONST_KEY_SET_YES = "yes"
	CONST_ORDER_LOWEST_AVAILABLE = "lowest-available"
