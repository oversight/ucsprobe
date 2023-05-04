import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorHostMgmtCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorHostMgmtCap")

	@staticmethod
	def ClassId():
		return "adaptorHostMgmtCap"

	DN = "Dn"
	MODE = "Mode"
	OPER_POWER_REQUIREMENT = "OperPowerRequirement"
	PREBOOT = "Preboot"
	PRESENCE = "Presence"
	REBOOT_ACTION_ON_DESTRUCTIVE = "RebootActionOnDestructive"
	RN = "Rn"
	STATUS = "Status"

	CONST_MODE_FULL = "full"
	CONST_MODE_PARTIAL = "partial"
	CONST_OPER_POWER_REQUIREMENT_FULL = "full"
	CONST_OPER_POWER_REQUIREMENT_NONE = "none"
	CONST_OPER_POWER_REQUIREMENT_STANDBY = "standby"
	CONST_PREBOOT_EFI = "EFI"
	CONST_PREBOOT_PNU_OS = "PnuOS"
	CONST_PREBOOT_NONE = "none"
	CONST_PRESENCE_CIMC = "cimc"
	CONST_PRESENCE_HOST = "host"
	CONST_PRESENCE_UNSPECIFIED = "unspecified"
	CONST_REBOOT_ACTION_ON_DESTRUCTIVE_ADAPTOR = "adaptor"
	CONST_REBOOT_ACTION_ON_DESTRUCTIVE_HOST = "host"
	CONST_REBOOT_ACTION_ON_DESTRUCTIVE_NONE = "none"
