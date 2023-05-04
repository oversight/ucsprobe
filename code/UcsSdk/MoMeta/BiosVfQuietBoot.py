import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfQuietBoot(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfQuietBoot")

	@staticmethod
	def ClassId():
		return "biosVfQuietBoot"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_QUIET_BOOT = "VpQuietBoot"

	CONST_VP_QUIET_BOOT_DISABLED = "disabled"
	CONST_VP_QUIET_BOOT_ENABLED = "enabled"
	CONST_VP_QUIET_BOOT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_QUIET_BOOT_PLATFORM_RECOMMENDED = "platform-recommended"
