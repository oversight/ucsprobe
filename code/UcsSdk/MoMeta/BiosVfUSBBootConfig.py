import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfUSBBootConfig(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfUSBBootConfig")

	@staticmethod
	def ClassId():
		return "biosVfUSBBootConfig"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_LEGACY_USBSUPPORT = "VpLegacyUSBSupport"
	VP_MAKE_DEVICE_NON_BOOTABLE = "VpMakeDeviceNonBootable"

	CONST_VP_LEGACY_USBSUPPORT_AUTO = "auto"
	CONST_VP_LEGACY_USBSUPPORT_DISABLED = "disabled"
	CONST_VP_LEGACY_USBSUPPORT_ENABLED = "enabled"
	CONST_VP_LEGACY_USBSUPPORT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_LEGACY_USBSUPPORT_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_MAKE_DEVICE_NON_BOOTABLE_DISABLED = "disabled"
	CONST_VP_MAKE_DEVICE_NON_BOOTABLE_ENABLED = "enabled"
	CONST_VP_MAKE_DEVICE_NON_BOOTABLE_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_MAKE_DEVICE_NON_BOOTABLE_PLATFORM_RECOMMENDED = "platform-recommended"
