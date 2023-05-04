import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfMemoryMappedIOAbove4GB(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfMemoryMappedIOAbove4GB")

	@staticmethod
	def ClassId():
		return "biosVfMemoryMappedIOAbove4GB"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_MEMORY_MAPPED_IOABOVE4_GB = "VpMemoryMappedIOAbove4GB"

	CONST_VP_MEMORY_MAPPED_IOABOVE4_GB_DISABLED = "disabled"
	CONST_VP_MEMORY_MAPPED_IOABOVE4_GB_ENABLED = "enabled"
	CONST_VP_MEMORY_MAPPED_IOABOVE4_GB_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_MEMORY_MAPPED_IOABOVE4_GB_PLATFORM_RECOMMENDED = "platform-recommended"
