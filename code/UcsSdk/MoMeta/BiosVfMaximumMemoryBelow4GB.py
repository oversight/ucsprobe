import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfMaximumMemoryBelow4GB(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfMaximumMemoryBelow4GB")

	@staticmethod
	def ClassId():
		return "biosVfMaximumMemoryBelow4GB"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_MAXIMUM_MEMORY_BELOW4_GB = "VpMaximumMemoryBelow4GB"

	CONST_VP_MAXIMUM_MEMORY_BELOW4_GB_DISABLED = "disabled"
	CONST_VP_MAXIMUM_MEMORY_BELOW4_GB_ENABLED = "enabled"
	CONST_VP_MAXIMUM_MEMORY_BELOW4_GB_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_MAXIMUM_MEMORY_BELOW4_GB_PLATFORM_RECOMMENDED = "platform-recommended"
