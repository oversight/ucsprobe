import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaUserRole(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaUserRole")

	@staticmethod
	def ClassId():
		return "aaaUserRole"

	CONFIG_STATE = "ConfigState"
	CONFIG_STATUS_MESSAGE = "ConfigStatusMessage"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_CONFIG_STATE_OK = "ok"
