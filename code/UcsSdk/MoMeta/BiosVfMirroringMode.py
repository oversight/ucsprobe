import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfMirroringMode(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfMirroringMode")

	@staticmethod
	def ClassId():
		return "biosVfMirroringMode"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_MIRRORING_MODE = "VpMirroringMode"

	CONST_VP_MIRRORING_MODE_INTER_SOCKET = "inter-socket"
	CONST_VP_MIRRORING_MODE_INTRA_SOCKET = "intra-socket"
	CONST_VP_MIRRORING_MODE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_MIRRORING_MODE_PLATFORM_RECOMMENDED = "platform-recommended"
