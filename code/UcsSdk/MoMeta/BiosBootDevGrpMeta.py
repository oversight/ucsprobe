import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Descr":UcsPropertyMeta("Descr", "descr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"DeviceName":UcsPropertyMeta("DeviceName", "deviceName", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"ErrVal":UcsPropertyMeta("ErrVal", "errVal", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["FAILURE", "SUCCESS"], ["0-4294967295"]),
	"Order":UcsPropertyMeta("Order", "order", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, None, None, None, ["1", "2", "3", "4", "5", "6", "7"], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["bev-order", "cd-order", "cimc-vmedia-cdd-device-order", "cimc-vmedia-fdd-device-order", "cimc-vmedia-hdd-device-order", "external-usb-device-order", "fdd-order", "hdd-order", "internal-efi-shell", "internal-usb-device-order", "iscsi-any-device-order", "iscsi-device-order", "kvm-vmedia-cdd-device-order", "kvm-vmedia-fdd-device-order", "kvm-vmedia-hdd-device-order", "lan-any-device-order", "local-storage-any-device-order", "network-device-order", "san-any-device-order", "san-device-order", "sdcard-device-order", "system-boot-order", "uefi-target-device-order", "unknown-device-order"], ["0-4294967295"]),
	"Meta":UcsMoMeta("BiosBootDevGrp", "biosBootDevGrp", "bdg-[Order]", _VersionMeta.Version101e, "InputOutput", 0x1fL, [], [u'biosBootDev'], ["Get"], ["read-only"])
}

