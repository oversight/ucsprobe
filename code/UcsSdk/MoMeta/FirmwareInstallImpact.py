import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareInstallImpact(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareInstallImpact")

	@staticmethod
	def ClassId():
		return "firmwareInstallImpact"

	DESCR = "Descr"
	DN = "Dn"
	KEY_DN = "KeyDn"
	MAINT_POLICY_DN = "MaintPolicyDn"
	REBOOT_POLICY = "RebootPolicy"
	RN = "Rn"
	STATUS = "Status"
	SUBJECT = "Subject"
	TYPE = "Type"

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
	CONST_TYPE_ACTIVATE = "activate"
	CONST_TYPE_NOIMPACT = "noimpact"
	CONST_TYPE_RESET = "reset"
	CONST_TYPE_UPDATE = "update"
