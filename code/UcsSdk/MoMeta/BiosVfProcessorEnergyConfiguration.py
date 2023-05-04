import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfProcessorEnergyConfiguration(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfProcessorEnergyConfiguration")

	@staticmethod
	def ClassId():
		return "biosVfProcessorEnergyConfiguration"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_ENERGY_PERFORMANCE = "VpEnergyPerformance"
	VP_POWER_TECHNOLOGY = "VpPowerTechnology"

	CONST_VP_ENERGY_PERFORMANCE_BALANCED_ENERGY = "balanced-energy"
	CONST_VP_ENERGY_PERFORMANCE_BALANCED_PERFORMANCE = "balanced-performance"
	CONST_VP_ENERGY_PERFORMANCE_ENERGY_EFFICIENT = "energy-efficient"
	CONST_VP_ENERGY_PERFORMANCE_PERFORMANCE = "performance"
	CONST_VP_ENERGY_PERFORMANCE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_ENERGY_PERFORMANCE_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_POWER_TECHNOLOGY_CUSTOM = "custom"
	CONST_VP_POWER_TECHNOLOGY_DISABLED = "disabled"
	CONST_VP_POWER_TECHNOLOGY_ENERGY_EFFICIENT = "energy-efficient"
	CONST_VP_POWER_TECHNOLOGY_PERFORMANCE = "performance"
	CONST_VP_POWER_TECHNOLOGY_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_POWER_TECHNOLOGY_PLATFORM_RECOMMENDED = "platform-recommended"
