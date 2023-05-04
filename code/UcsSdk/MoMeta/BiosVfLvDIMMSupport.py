import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfLvDIMMSupport(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfLvDIMMSupport")

	@staticmethod
	def ClassId():
		return "biosVfLvDIMMSupport"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_LV_DDRMODE = "VpLvDDRMode"

	CONST_VP_LV_DDRMODE_AUTO = "auto"
	CONST_VP_LV_DDRMODE_PERFORMANCE_MODE = "performance-mode"
	CONST_VP_LV_DDRMODE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_LV_DDRMODE_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_LV_DDRMODE_POWER_SAVING_MODE = "power-saving-mode"
