import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareCatalogue(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareCatalogue")

	@staticmethod
	def ClassId():
		return "firmwareCatalogue"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	SYNC_TRIGGER = "SyncTrigger"

	CONST_SYNC_TRIGGER_FALSE = "false"
	CONST_SYNC_TRIGGER_NO = "no"
	CONST_SYNC_TRIGGER_TRUE = "true"
	CONST_SYNC_TRIGGER_YES = "yes"
