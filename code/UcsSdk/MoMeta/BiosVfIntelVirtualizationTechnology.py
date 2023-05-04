import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfIntelVirtualizationTechnology(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfIntelVirtualizationTechnology")

	@staticmethod
	def ClassId():
		return "biosVfIntelVirtualizationTechnology"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_INTEL_VIRTUALIZATION_TECHNOLOGY = "VpIntelVirtualizationTechnology"

	CONST_VP_INTEL_VIRTUALIZATION_TECHNOLOGY_DISABLED = "disabled"
	CONST_VP_INTEL_VIRTUALIZATION_TECHNOLOGY_ENABLED = "enabled"
	CONST_VP_INTEL_VIRTUALIZATION_TECHNOLOGY_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_INTEL_VIRTUALIZATION_TECHNOLOGY_PLATFORM_RECOMMENDED = "platform-recommended"
