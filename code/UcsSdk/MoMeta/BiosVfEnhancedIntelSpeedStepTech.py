import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfEnhancedIntelSpeedStepTech(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfEnhancedIntelSpeedStepTech")

	@staticmethod
	def ClassId():
		return "biosVfEnhancedIntelSpeedStepTech"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_ENHANCED_INTEL_SPEED_STEP_TECH = "VpEnhancedIntelSpeedStepTech"

	CONST_VP_ENHANCED_INTEL_SPEED_STEP_TECH_DISABLED = "disabled"
	CONST_VP_ENHANCED_INTEL_SPEED_STEP_TECH_ENABLED = "enabled"
	CONST_VP_ENHANCED_INTEL_SPEED_STEP_TECH_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_ENHANCED_INTEL_SPEED_STEP_TECH_PLATFORM_RECOMMENDED = "platform-recommended"
