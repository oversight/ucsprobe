import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfProcessorCState(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfProcessorCState")

	@staticmethod
	def ClassId():
		return "biosVfProcessorCState"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_PROCESSOR_CSTATE = "VpProcessorCState"

	CONST_VP_PROCESSOR_CSTATE_DISABLED = "disabled"
	CONST_VP_PROCESSOR_CSTATE_ENABLED = "enabled"
	CONST_VP_PROCESSOR_CSTATE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_PROCESSOR_CSTATE_PLATFORM_RECOMMENDED = "platform-recommended"
