import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"BootOrderType":UcsPropertyMeta("BootOrderType", "bootOrderType", "string", _VersionMeta.Version202m, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["bev-order", "cd-order", "cimc-vmedia-cdd-device-order", "cimc-vmedia-fdd-device-order", "cimc-vmedia-hdd-device-order", "external-usb-device-order", "fdd-order", "hdd-order", "internal-efi-shell", "internal-usb-device-order", "iscsi-any-device-order", "iscsi-device-order", "kvm-vmedia-cdd-device-order", "kvm-vmedia-fdd-device-order", "kvm-vmedia-hdd-device-order", "lan-any-device-order", "local-storage-any-device-order", "network-device-order", "san-any-device-order", "san-device-order", "sdcard-device-order", "system-boot-order", "uefi-target-device-order", "unknown-device-order"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version201m, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"MacOffset1":UcsPropertyMeta("MacOffset1", "macOffset1", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x8L, None, None, None, [], ["0-4294967295"]),
	"MacOffset2":UcsPropertyMeta("MacOffset2", "macOffset2", "byte", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x10L, None, None, None, [], ["0-4294967295"]),
	"OffloadSupport":UcsPropertyMeta("OffloadSupport", "offloadSupport", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"OffloadType":UcsPropertyMeta("OffloadType", "offloadType", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x40L, None, None, None, ["none", "physical", "virtual"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, 0x80L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"VlanForBoot":UcsPropertyMeta("VlanForBoot", "vlanForBoot", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadWrite, 0x200L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"Meta":UcsMoMeta("AdaptorIScsiCap", "adaptorIScsiCap", "iscsi", _VersionMeta.Version201m, "InputOutput", 0x3ffL, [], [], ["Get"], ["read-only"])
}

