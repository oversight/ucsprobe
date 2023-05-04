import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfIntelHyperThreadingTech(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfIntelHyperThreadingTech")

	@staticmethod
	def ClassId():
		return "biosVfIntelHyperThreadingTech"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_INTEL_HYPER_THREADING_TECH = "VpIntelHyperThreadingTech"

	CONST_VP_INTEL_HYPER_THREADING_TECH_DISABLED = "disabled"
	CONST_VP_INTEL_HYPER_THREADING_TECH_ENABLED = "enabled"
	CONST_VP_INTEL_HYPER_THREADING_TECH_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_INTEL_HYPER_THREADING_TECH_PLATFORM_RECOMMENDED = "platform-recommended"
