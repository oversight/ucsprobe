import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfNUMAOptimized(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfNUMAOptimized")

	@staticmethod
	def ClassId():
		return "biosVfNUMAOptimized"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_NUMAOPTIMIZED = "VpNUMAOptimized"

	CONST_VP_NUMAOPTIMIZED_DISABLED = "disabled"
	CONST_VP_NUMAOPTIMIZED_ENABLED = "enabled"
	CONST_VP_NUMAOPTIMIZED_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_NUMAOPTIMIZED_PLATFORM_RECOMMENDED = "platform-recommended"
