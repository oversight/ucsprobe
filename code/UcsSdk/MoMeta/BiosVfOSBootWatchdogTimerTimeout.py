import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfOSBootWatchdogTimerTimeout(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfOSBootWatchdogTimerTimeout")

	@staticmethod
	def ClassId():
		return "biosVfOSBootWatchdogTimerTimeout"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT = "VpOSBootWatchdogTimerTimeout"

	CONST_VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_10_MINUTES = "10-minutes"
	CONST_VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_15_MINUTES = "15-minutes"
	CONST_VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_20_MINUTES = "20-minutes"
	CONST_VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_5_MINUTES = "5-minutes"
	CONST_VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_PLATFORM_RECOMMENDED = "platform-recommended"
