import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfIntelEntrySASRAIDModule(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfIntelEntrySASRAIDModule")

	@staticmethod
	def ClassId():
		return "biosVfIntelEntrySASRAIDModule"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_SASRAID = "VpSASRAID"
	VP_SASRAIDMODULE = "VpSASRAIDModule"

	CONST_VP_SASRAID_DISABLED = "disabled"
	CONST_VP_SASRAID_ENABLED = "enabled"
	CONST_VP_SASRAID_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_SASRAID_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_SASRAIDMODULE_INTEL_ESRTII = "intel-esrtii"
	CONST_VP_SASRAIDMODULE_IT_IR_RAID = "it-ir-raid"
	CONST_VP_SASRAIDMODULE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_SASRAIDMODULE_PLATFORM_RECOMMENDED = "platform-recommended"
