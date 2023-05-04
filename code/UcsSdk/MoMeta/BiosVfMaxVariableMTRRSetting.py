import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfMaxVariableMTRRSetting(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfMaxVariableMTRRSetting")

	@staticmethod
	def ClassId():
		return "biosVfMaxVariableMTRRSetting"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_PROCESSOR_MTRR = "VpProcessorMtrr"

	CONST_VP_PROCESSOR_MTRR_8 = "8"
	CONST_VP_PROCESSOR_MTRR_AUTO_MAX = "auto-max"
	CONST_VP_PROCESSOR_MTRR_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_PROCESSOR_MTRR_PLATFORM_RECOMMENDED = "platform-recommended"
