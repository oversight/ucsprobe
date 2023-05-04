import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfSelectMemoryRASConfiguration(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfSelectMemoryRASConfiguration")

	@staticmethod
	def ClassId():
		return "biosVfSelectMemoryRASConfiguration"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_SELECT_MEMORY_RASCONFIGURATION = "VpSelectMemoryRASConfiguration"

	CONST_VP_SELECT_MEMORY_RASCONFIGURATION_LOCKSTEP = "lockstep"
	CONST_VP_SELECT_MEMORY_RASCONFIGURATION_MAXIMUM_PERFORMANCE = "maximum-performance"
	CONST_VP_SELECT_MEMORY_RASCONFIGURATION_MIRRORING = "mirroring"
	CONST_VP_SELECT_MEMORY_RASCONFIGURATION_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_SELECT_MEMORY_RASCONFIGURATION_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_SELECT_MEMORY_RASCONFIGURATION_SPARING = "sparing"
