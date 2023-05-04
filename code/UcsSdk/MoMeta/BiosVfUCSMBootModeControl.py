import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfUCSMBootModeControl(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfUCSMBootModeControl")

	@staticmethod
	def ClassId():
		return "biosVfUCSMBootModeControl"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_UEFIBOOT_MODE = "VpUEFIBootMode"

	CONST_VP_UEFIBOOT_MODE_DISABLED = "disabled"
	CONST_VP_UEFIBOOT_MODE_ENABLED = "enabled"
	CONST_VP_UEFIBOOT_MODE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_UEFIBOOT_MODE_PLATFORM_RECOMMENDED = "platform-recommended"
