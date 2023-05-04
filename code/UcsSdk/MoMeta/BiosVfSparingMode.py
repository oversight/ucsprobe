import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfSparingMode(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfSparingMode")

	@staticmethod
	def ClassId():
		return "biosVfSparingMode"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_SPARING_MODE = "VpSparingMode"

	CONST_VP_SPARING_MODE_DIMM_SPARING = "dimm-sparing"
	CONST_VP_SPARING_MODE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_SPARING_MODE_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_SPARING_MODE_RANK_SPARING = "rank-sparing"
