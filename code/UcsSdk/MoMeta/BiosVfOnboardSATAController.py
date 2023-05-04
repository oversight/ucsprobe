import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfOnboardSATAController(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfOnboardSATAController")

	@staticmethod
	def ClassId():
		return "biosVfOnboardSATAController"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_ONBOARD_SATACONTROLLER = "VpOnboardSATAController"
	VP_SATAMODE = "VpSATAMode"

	CONST_VP_ONBOARD_SATACONTROLLER_DISABLED = "disabled"
	CONST_VP_ONBOARD_SATACONTROLLER_ENABLED = "enabled"
	CONST_VP_ONBOARD_SATACONTROLLER_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_ONBOARD_SATACONTROLLER_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_SATAMODE_AHCI = "ahci"
	CONST_VP_SATAMODE_COMPATIBILITY = "compatibility"
	CONST_VP_SATAMODE_ENHANCED = "enhanced"
	CONST_VP_SATAMODE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_SATAMODE_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_SATAMODE_SW_RAID = "sw-raid"
