import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaSshAuth(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaSshAuth")

	@staticmethod
	def ClassId():
		return "aaaSshAuth"

	DATA = "Data"
	DN = "Dn"
	OLD_STR_TYPE = "OldStrType"
	RN = "Rn"
	STATUS = "Status"
	STR_TYPE = "StrType"

	CONST_OLD_STR_TYPE_KEY = "key"
	CONST_OLD_STR_TYPE_NONE = "none"
	CONST_STR_TYPE_KEY = "key"
	CONST_STR_TYPE_NONE = "none"
