import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfProcessorC1E(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfProcessorC1E")

	@staticmethod
	def ClassId():
		return "biosVfProcessorC1E"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_PROCESSOR_C1_E = "VpProcessorC1E"

	CONST_VP_PROCESSOR_C1_E_DISABLED = "disabled"
	CONST_VP_PROCESSOR_C1_E_ENABLED = "enabled"
	CONST_VP_PROCESSOR_C1_E_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_PROCESSOR_C1_E_PLATFORM_RECOMMENDED = "platform-recommended"
