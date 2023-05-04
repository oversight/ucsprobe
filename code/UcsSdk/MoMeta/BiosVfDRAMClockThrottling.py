import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfDRAMClockThrottling(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfDRAMClockThrottling")

	@staticmethod
	def ClassId():
		return "biosVfDRAMClockThrottling"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_DRAMCLOCK_THROTTLING = "VpDRAMClockThrottling"

	CONST_VP_DRAMCLOCK_THROTTLING_AUTO = "auto"
	CONST_VP_DRAMCLOCK_THROTTLING_BALANCED = "balanced"
	CONST_VP_DRAMCLOCK_THROTTLING_ENERGY_EFFICIENT = "energy-efficient"
	CONST_VP_DRAMCLOCK_THROTTLING_PERFORMANCE = "performance"
	CONST_VP_DRAMCLOCK_THROTTLING_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_DRAMCLOCK_THROTTLING_PLATFORM_RECOMMENDED = "platform-recommended"
