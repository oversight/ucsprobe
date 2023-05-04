import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaProviderGroup(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaProviderGroup")

	@staticmethod
	def ClassId():
		return "aaaProviderGroup"

	CONFIG_STATE = "ConfigState"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	SIZE = "Size"
	STATUS = "Status"

	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_CONFIG_STATE_OK = "ok"
