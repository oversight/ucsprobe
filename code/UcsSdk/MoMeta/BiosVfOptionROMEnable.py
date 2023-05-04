import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfOptionROMEnable(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfOptionROMEnable")

	@staticmethod
	def ClassId():
		return "biosVfOptionROMEnable"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_STATE = "VpState"

	CONST_VP_STATE_DISABLED = "disabled"
	CONST_VP_STATE_ENABLED = "enabled"
	CONST_VP_STATE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_STATE_PLATFORM_RECOMMENDED = "platform-recommended"
