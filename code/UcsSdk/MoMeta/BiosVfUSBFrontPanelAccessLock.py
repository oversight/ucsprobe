import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfUSBFrontPanelAccessLock(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfUSBFrontPanelAccessLock")

	@staticmethod
	def ClassId():
		return "biosVfUSBFrontPanelAccessLock"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_USBFRONT_PANEL_LOCK = "VpUSBFrontPanelLock"

	CONST_VP_USBFRONT_PANEL_LOCK_DISABLED = "disabled"
	CONST_VP_USBFRONT_PANEL_LOCK_ENABLED = "enabled"
	CONST_VP_USBFRONT_PANEL_LOCK_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_USBFRONT_PANEL_LOCK_PLATFORM_RECOMMENDED = "platform-recommended"
