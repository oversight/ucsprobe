import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorIScsiCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorIScsiCap")

	@staticmethod
	def ClassId():
		return "adaptorIScsiCap"

	BOOT_ORDER_TYPE = "BootOrderType"
	DN = "Dn"
	MAC_OFFSET1 = "MacOffset1"
	MAC_OFFSET2 = "MacOffset2"
	OFFLOAD_SUPPORT = "OffloadSupport"
	OFFLOAD_TYPE = "OffloadType"
	RN = "Rn"
	STATUS = "Status"
	VLAN_FOR_BOOT = "VlanForBoot"

	CONST_BOOT_ORDER_TYPE_BEV_ORDER = "bev-order"
	CONST_BOOT_ORDER_TYPE_CD_ORDER = "cd-order"
	CONST_BOOT_ORDER_TYPE_CIMC_VMEDIA_CDD_DEVICE_ORDER = "cimc-vmedia-cdd-device-order"
	CONST_BOOT_ORDER_TYPE_CIMC_VMEDIA_FDD_DEVICE_ORDER = "cimc-vmedia-fdd-device-order"
	CONST_BOOT_ORDER_TYPE_CIMC_VMEDIA_HDD_DEVICE_ORDER = "cimc-vmedia-hdd-device-order"
	CONST_BOOT_ORDER_TYPE_EXTERNAL_USB_DEVICE_ORDER = "external-usb-device-order"
	CONST_BOOT_ORDER_TYPE_FDD_ORDER = "fdd-order"
	CONST_BOOT_ORDER_TYPE_HDD_ORDER = "hdd-order"
	CONST_BOOT_ORDER_TYPE_INTERNAL_EFI_SHELL = "internal-efi-shell"
	CONST_BOOT_ORDER_TYPE_INTERNAL_USB_DEVICE_ORDER = "internal-usb-device-order"
	CONST_BOOT_ORDER_TYPE_ISCSI_ANY_DEVICE_ORDER = "iscsi-any-device-order"
	CONST_BOOT_ORDER_TYPE_ISCSI_DEVICE_ORDER = "iscsi-device-order"
	CONST_BOOT_ORDER_TYPE_KVM_VMEDIA_CDD_DEVICE_ORDER = "kvm-vmedia-cdd-device-order"
	CONST_BOOT_ORDER_TYPE_KVM_VMEDIA_FDD_DEVICE_ORDER = "kvm-vmedia-fdd-device-order"
	CONST_BOOT_ORDER_TYPE_KVM_VMEDIA_HDD_DEVICE_ORDER = "kvm-vmedia-hdd-device-order"
	CONST_BOOT_ORDER_TYPE_LAN_ANY_DEVICE_ORDER = "lan-any-device-order"
	CONST_BOOT_ORDER_TYPE_LOCAL_STORAGE_ANY_DEVICE_ORDER = "local-storage-any-device-order"
	CONST_BOOT_ORDER_TYPE_NETWORK_DEVICE_ORDER = "network-device-order"
	CONST_BOOT_ORDER_TYPE_SAN_ANY_DEVICE_ORDER = "san-any-device-order"
	CONST_BOOT_ORDER_TYPE_SAN_DEVICE_ORDER = "san-device-order"
	CONST_BOOT_ORDER_TYPE_SDCARD_DEVICE_ORDER = "sdcard-device-order"
	CONST_BOOT_ORDER_TYPE_SYSTEM_BOOT_ORDER = "system-boot-order"
	CONST_BOOT_ORDER_TYPE_UEFI_TARGET_DEVICE_ORDER = "uefi-target-device-order"
	CONST_BOOT_ORDER_TYPE_UNKNOWN_DEVICE_ORDER = "unknown-device-order"
	CONST_OFFLOAD_SUPPORT_FALSE = "false"
	CONST_OFFLOAD_SUPPORT_NO = "no"
	CONST_OFFLOAD_SUPPORT_TRUE = "true"
	CONST_OFFLOAD_SUPPORT_YES = "yes"
	CONST_OFFLOAD_TYPE_NONE = "none"
	CONST_OFFLOAD_TYPE_PHYSICAL = "physical"
	CONST_OFFLOAD_TYPE_VIRTUAL = "virtual"
	CONST_VLAN_FOR_BOOT_FALSE = "false"
	CONST_VLAN_FOR_BOOT_NO = "no"
	CONST_VLAN_FOR_BOOT_TRUE = "true"
	CONST_VLAN_FOR_BOOT_YES = "yes"
