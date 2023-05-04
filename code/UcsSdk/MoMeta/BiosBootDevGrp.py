import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosBootDevGrp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosBootDevGrp")

	@staticmethod
	def ClassId():
		return "biosBootDevGrp"

	DESCR = "Descr"
	DEVICE_NAME = "DeviceName"
	DN = "Dn"
	ERR_VAL = "ErrVal"
	ORDER = "Order"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_ERR_VAL_FAILURE = "FAILURE"
	CONST_ERR_VAL_SUCCESS = "SUCCESS"
	CONST_ORDER_1 = "1"
	CONST_ORDER_2 = "2"
	CONST_ORDER_3 = "3"
	CONST_ORDER_4 = "4"
	CONST_ORDER_5 = "5"
	CONST_ORDER_6 = "6"
	CONST_ORDER_7 = "7"
	CONST_TYPE_BEV_ORDER = "bev-order"
	CONST_TYPE_CD_ORDER = "cd-order"
	CONST_TYPE_CIMC_VMEDIA_CDD_DEVICE_ORDER = "cimc-vmedia-cdd-device-order"
	CONST_TYPE_CIMC_VMEDIA_FDD_DEVICE_ORDER = "cimc-vmedia-fdd-device-order"
	CONST_TYPE_CIMC_VMEDIA_HDD_DEVICE_ORDER = "cimc-vmedia-hdd-device-order"
	CONST_TYPE_EXTERNAL_USB_DEVICE_ORDER = "external-usb-device-order"
	CONST_TYPE_FDD_ORDER = "fdd-order"
	CONST_TYPE_HDD_ORDER = "hdd-order"
	CONST_TYPE_INTERNAL_EFI_SHELL = "internal-efi-shell"
	CONST_TYPE_INTERNAL_USB_DEVICE_ORDER = "internal-usb-device-order"
	CONST_TYPE_ISCSI_ANY_DEVICE_ORDER = "iscsi-any-device-order"
	CONST_TYPE_ISCSI_DEVICE_ORDER = "iscsi-device-order"
	CONST_TYPE_KVM_VMEDIA_CDD_DEVICE_ORDER = "kvm-vmedia-cdd-device-order"
	CONST_TYPE_KVM_VMEDIA_FDD_DEVICE_ORDER = "kvm-vmedia-fdd-device-order"
	CONST_TYPE_KVM_VMEDIA_HDD_DEVICE_ORDER = "kvm-vmedia-hdd-device-order"
	CONST_TYPE_LAN_ANY_DEVICE_ORDER = "lan-any-device-order"
	CONST_TYPE_LOCAL_STORAGE_ANY_DEVICE_ORDER = "local-storage-any-device-order"
	CONST_TYPE_NETWORK_DEVICE_ORDER = "network-device-order"
	CONST_TYPE_SAN_ANY_DEVICE_ORDER = "san-any-device-order"
	CONST_TYPE_SAN_DEVICE_ORDER = "san-device-order"
	CONST_TYPE_SDCARD_DEVICE_ORDER = "sdcard-device-order"
	CONST_TYPE_SYSTEM_BOOT_ORDER = "system-boot-order"
	CONST_TYPE_UEFI_TARGET_DEVICE_ORDER = "uefi-target-device-order"
	CONST_TYPE_UNKNOWN_DEVICE_ORDER = "unknown-device-order"
