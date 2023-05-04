import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfFrontPanelLockout(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfFrontPanelLockout")

	@staticmethod
	def ClassId():
		return "biosVfFrontPanelLockout"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_FRONT_PANEL_LOCKOUT = "VpFrontPanelLockout"

	CONST_VP_FRONT_PANEL_LOCKOUT_DISABLED = "disabled"
	CONST_VP_FRONT_PANEL_LOCKOUT_ENABLED = "enabled"
	CONST_VP_FRONT_PANEL_LOCKOUT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_FRONT_PANEL_LOCKOUT_PLATFORM_RECOMMENDED = "platform-recommended"
