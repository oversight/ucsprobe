import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfACPI10Support(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfACPI10Support")

	@staticmethod
	def ClassId():
		return "biosVfACPI10Support"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_ACPI10_SUPPORT = "VpACPI10Support"

	CONST_VP_ACPI10_SUPPORT_DISABLED = "disabled"
	CONST_VP_ACPI10_SUPPORT_ENABLED = "enabled"
	CONST_VP_ACPI10_SUPPORT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_ACPI10_SUPPORT_PLATFORM_RECOMMENDED = "platform-recommended"
