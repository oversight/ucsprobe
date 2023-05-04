import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVfUSBPortConfiguration(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVfUSBPortConfiguration")

	@staticmethod
	def ClassId():
		return "biosVfUSBPortConfiguration"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	VP_PORT6064_EMULATION = "VpPort6064Emulation"
	VP_USBPORT_FRONT = "VpUSBPortFront"
	VP_USBPORT_INTERNAL = "VpUSBPortInternal"
	VP_USBPORT_KVM = "VpUSBPortKVM"
	VP_USBPORT_REAR = "VpUSBPortRear"
	VP_USBPORT_SDCARD = "VpUSBPortSDCard"
	VP_USBPORT_VMEDIA = "VpUSBPortVMedia"

	CONST_VP_PORT6064_EMULATION_DISABLED = "disabled"
	CONST_VP_PORT6064_EMULATION_ENABLED = "enabled"
	CONST_VP_PORT6064_EMULATION_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_PORT6064_EMULATION_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_USBPORT_FRONT_DISABLED = "disabled"
	CONST_VP_USBPORT_FRONT_ENABLED = "enabled"
	CONST_VP_USBPORT_FRONT_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_USBPORT_FRONT_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_USBPORT_INTERNAL_DISABLED = "disabled"
	CONST_VP_USBPORT_INTERNAL_ENABLED = "enabled"
	CONST_VP_USBPORT_INTERNAL_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_USBPORT_INTERNAL_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_USBPORT_KVM_DISABLED = "disabled"
	CONST_VP_USBPORT_KVM_ENABLED = "enabled"
	CONST_VP_USBPORT_KVM_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_USBPORT_KVM_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_USBPORT_REAR_DISABLED = "disabled"
	CONST_VP_USBPORT_REAR_ENABLED = "enabled"
	CONST_VP_USBPORT_REAR_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_USBPORT_REAR_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_USBPORT_SDCARD_DISABLED = "disabled"
	CONST_VP_USBPORT_SDCARD_ENABLED = "enabled"
	CONST_VP_USBPORT_SDCARD_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_USBPORT_SDCARD_PLATFORM_RECOMMENDED = "platform-recommended"
	CONST_VP_USBPORT_VMEDIA_DISABLED = "disabled"
	CONST_VP_USBPORT_VMEDIA_ENABLED = "enabled"
	CONST_VP_USBPORT_VMEDIA_PLATFORM_DEFAULT = "platform-default"
	CONST_VP_USBPORT_VMEDIA_PLATFORM_RECOMMENDED = "platform-recommended"
