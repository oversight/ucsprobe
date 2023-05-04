import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfOSBootWatchdogTimer(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfOSBootWatchdogTimer")

	@staticmethod
	def ClassId():
		return "biosVfOSBootWatchdogTimer"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_OSBOOT_WATCHDOG_TIMER = "VpOSBootWatchdogTimer"

	CONST_VP_OSBOOT_WATCHDOG_TIMER_DISABLED = "disabled"
	CONST_VP_OSBOOT_WATCHDOG_TIMER_ENABLED = "enabled"
	CONST_VP_OSBOOT_WATCHDOG_TIMER_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_OSBOOT_WATCHDOG_TIMER_PLATFORM_RECOMMENDED = "platform-recommended"
