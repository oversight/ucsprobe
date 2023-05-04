import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfAllUSBDevices(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfAllUSBDevices")

	@staticmethod
	def ClassId():
		return "biosVfAllUSBDevices"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_ALL_USBDEVICES = "VpAllUSBDevices"

	CONST_VP_ALL_USBDEVICES_DISABLED = "disabled"
	CONST_VP_ALL_USBDEVICES_ENABLED = "enabled"
	CONST_VP_ALL_USBDEVICES_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_ALL_USBDEVICES_PLATFORM_RECOMMENDED = "platform-recommended"
