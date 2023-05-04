import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IdentSysInfo(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IdentSysInfo")

	@staticmethod
	def ClassId():
		return "identSysInfo"

	DN = "Dn"
	GENERATION = "Generation"
	IS_SYNC = "IsSync"
	IS_SYNC_ALLOWED = "IsSyncAllowed"
	RN = "Rn"
	STATUS = "Status"

	CONST_IS_SYNC_FALSE = "false"
	CONST_IS_SYNC_NO = "no"
	CONST_IS_SYNC_TRUE = "true"
	CONST_IS_SYNC_YES = "yes"
	CONST_IS_SYNC_ALLOWED_FALSE = "false"
	CONST_IS_SYNC_ALLOWED_NO = "no"
	CONST_IS_SYNC_ALLOWED_TRUE = "true"
	CONST_IS_SYNC_ALLOWED_YES = "yes"
