import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfExecuteDisableBit(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfExecuteDisableBit")

	@staticmethod
	def ClassId():
		return "biosVfExecuteDisableBit"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_EXECUTE_DISABLE_BIT = "VpExecuteDisableBit"

	CONST_VP_EXECUTE_DISABLE_BIT_DISABLED = "disabled"
	CONST_VP_EXECUTE_DISABLE_BIT_ENABLED = "enabled"
	CONST_VP_EXECUTE_DISABLE_BIT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_EXECUTE_DISABLE_BIT_PLATFORM_RECOMMENDED = "platform-recommended"
