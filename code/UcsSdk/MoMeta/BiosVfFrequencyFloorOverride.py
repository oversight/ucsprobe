import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfFrequencyFloorOverride(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfFrequencyFloorOverride")

	@staticmethod
	def ClassId():
		return "biosVfFrequencyFloorOverride"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_FREQUENCY_FLOOR_OVERRIDE = "VpFrequencyFloorOverride"

	CONST_VP_FREQUENCY_FLOOR_OVERRIDE_DISABLED = "disabled"
	CONST_VP_FREQUENCY_FLOOR_OVERRIDE_ENABLED = "enabled"
	CONST_VP_FREQUENCY_FLOOR_OVERRIDE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_FREQUENCY_FLOOR_OVERRIDE_PLATFORM_RECOMMENDED = "platform-recommended"
