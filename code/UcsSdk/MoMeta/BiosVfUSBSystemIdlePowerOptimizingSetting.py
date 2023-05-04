import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfUSBSystemIdlePowerOptimizingSetting(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfUSBSystemIdlePowerOptimizingSetting")

	@staticmethod
	def ClassId():
		return "biosVfUSBSystemIdlePowerOptimizingSetting"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_USBIDLE_POWER_OPTIMIZING = "VpUSBIdlePowerOptimizing"

	CONST_VP_USBIDLE_POWER_OPTIMIZING_HIGH_PERFORMANCE = "high-performance"
	CONST_VP_USBIDLE_POWER_OPTIMIZING_LOWER_IDLE_POWER = "lower-idle-power"
	CONST_VP_USBIDLE_POWER_OPTIMIZING_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_USBIDLE_POWER_OPTIMIZING_PLATFORM_RECOMMENDED = "platform-recommended"
