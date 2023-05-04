import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApePalo(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApePalo")

	@staticmethod
	def ClassId():
		return "apePalo"

	DESCRIPTION = "Description"
	DN = "Dn"
	FRU_ID = "FruId"
	HW_VERSION = "HwVersion"
	MAC1 = "Mac1"
	MAC2 = "Mac2"
	NAME = "Name"
	RN = "Rn"
	SERIAL = "Serial"
	START_EVENT = "StartEvent"
	STATUS = "Status"
	SW_BACKUP_VERSION = "SwBackupVersion"
	SW_STARTUP_VERSION = "SwStartupVersion"
	SW_VERSION = "SwVersion"
	TYPE = "Type"

	CONST_TYPE_MENLO = "Menlo"
	CONST_TYPE_OPLIN = "Oplin"
	CONST_TYPE_PALO = "Palo"
	CONST_TYPE_UNKNOWN = "Unknown"
