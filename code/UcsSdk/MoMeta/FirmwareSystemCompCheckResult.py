import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareSystemCompCheckResult(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareSystemCompCheckResult")

	@staticmethod
	def ClassId():
		return "firmwareSystemCompCheckResult"

	DN = "Dn"
	KEY_DESCR = "KeyDescr"
	KEY_DN = "KeyDn"
	NON_COMP_DESCR = "NonCompDescr"
	NON_COMP_DNS = "NonCompDns"
	RN = "Rn"
	STATUS = "Status"
	SUBJECT = "Subject"

	CONST_SUBJECT_ADAPTOR = "adaptor"
	CONST_SUBJECT_BIOS = "bios"
	CONST_SUBJECT_BOARD_CONTROLLER = "board-controller"
	CONST_SUBJECT_CIMC = "cimc"
	CONST_SUBJECT_GRAPHICS_CARD = "graphics-card"
	CONST_SUBJECT_IOCARD = "iocard"
	CONST_SUBJECT_SERVER = "server"
	CONST_SUBJECT_SERVICE_PROFILE = "service-profile"
	CONST_SUBJECT_STORAGE_CONTROLLER = "storage-controller"
	CONST_SUBJECT_SWITCH = "switch"
	CONST_SUBJECT_SYSTEM = "system"
	CONST_SUBJECT_UNKNOWN = "unknown"
