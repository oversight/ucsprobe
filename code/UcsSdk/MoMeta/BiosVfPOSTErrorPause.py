import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfPOSTErrorPause(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfPOSTErrorPause")

	@staticmethod
	def ClassId():
		return "biosVfPOSTErrorPause"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_POSTERROR_PAUSE = "VpPOSTErrorPause"

	CONST_VP_POSTERROR_PAUSE_DISABLED = "disabled"
	CONST_VP_POSTERROR_PAUSE_ENABLED = "enabled"
	CONST_VP_POSTERROR_PAUSE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_POSTERROR_PAUSE_PLATFORM_RECOMMENDED = "platform-recommended"
