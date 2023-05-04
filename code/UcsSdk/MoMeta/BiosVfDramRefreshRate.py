import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfDramRefreshRate(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfDramRefreshRate")

	@staticmethod
	def ClassId():
		return "biosVfDramRefreshRate"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_DRAM_REFRESH_RATE = "VpDramRefreshRate"

	CONST_VP_DRAM_REFRESH_RATE_1X = "1x"
	CONST_VP_DRAM_REFRESH_RATE_2X = "2x"
	CONST_VP_DRAM_REFRESH_RATE_3X = "3x"
	CONST_VP_DRAM_REFRESH_RATE_4X = "4x"
	CONST_VP_DRAM_REFRESH_RATE_AUTO = "auto"
	CONST_VP_DRAM_REFRESH_RATE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_DRAM_REFRESH_RATE_PLATFORM_RECOMMENDED = "platform-recommended"
