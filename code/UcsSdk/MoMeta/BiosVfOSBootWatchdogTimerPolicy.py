import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfOSBootWatchdogTimerPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfOSBootWatchdogTimerPolicy")

	@staticmethod
	def ClassId():
		return "biosVfOSBootWatchdogTimerPolicy"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_OSBOOT_WATCHDOG_TIMER_POLICY = "VpOSBootWatchdogTimerPolicy"

	CONST_VP_OSBOOT_WATCHDOG_TIMER_POLICY_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_OSBOOT_WATCHDOG_TIMER_POLICY_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_OSBOOT_WATCHDOG_TIMER_POLICY_POWER_OFF = "power-off"
	CONST_VP_OSBOOT_WATCHDOG_TIMER_POLICY_RESET = "reset"
