import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AccessPolicy":UcsPropertyMeta("AccessPolicy", "accessPolicy", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["blocked", "read-only", "read-write", "unknown"], ["0-4294967295"]),
	"ActualWriteCachePolicy":UcsPropertyMeta("ActualWriteCachePolicy", "actualWriteCachePolicy", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unknown", "write-back", "write-through"], ["0-4294967295"]),
	"BlockSize":UcsPropertyMeta("BlockSize", "blockSize", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unknown"], ["0-4294967295"]),
	"Bootable":UcsPropertyMeta("Bootable", "bootable", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "true", "unknown"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version211a, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConfiguredWriteCachePolicy":UcsPropertyMeta("ConfiguredWriteCachePolicy", "configuredWriteCachePolicy", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["always-write-back", "unknown", "write-back-good-bbu", "write-through"], ["0-4294967295"]),
	"ConnectionProtocol":UcsPropertyMeta("ConnectionProtocol", "connectionProtocol", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["SAS", "SATA", "unspecified"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"DriveCache":UcsPropertyMeta("DriveCache", "driveCache", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["disable", "enable", "no-change", "unknown"], ["0-4294967295"]),
	"DriveState":UcsPropertyMeta("DriveState", "driveState", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["cache-degraded", "degraded", "offline", "optimal", "partially-degraded", "unknown"], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "uint", _VersionMeta.Version211a, UcsPropertyMeta.Naming, 0x4L, None, None, None, [], ["0-4294967295"]),
	"IoPolicy":UcsPropertyMeta("IoPolicy", "ioPolicy", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["cached", "direct", "unknown"], ["0-4294967295"]),
	"Lc":UcsPropertyMeta("Lc", "lc", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], ["0-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"NumberOfBlocks":UcsPropertyMeta("NumberOfBlocks", "numberOfBlocks", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unknown"], ["0-4294967295"]),
	"OperQualifierReason":UcsPropertyMeta("OperQualifierReason", "operQualifierReason", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Operability":UcsPropertyMeta("Operability", "operability", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
	"Presence":UcsPropertyMeta("Presence", "presence", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
	"ReadPolicy":UcsPropertyMeta("ReadPolicy", "readPolicy", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["normal", "read-ahead", "unknown"], ["0-4294967295"]),
	"Revision":UcsPropertyMeta("Revision", "revision", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Serial":UcsPropertyMeta("Serial", "serial", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Size":UcsPropertyMeta("Size", "size", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unknown"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"StripSize":UcsPropertyMeta("StripSize", "stripSize", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unknown"], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadWrite, 0x20L, None, None, None, ["mirror", "mirror-stripe", "raid", "simple", "stripe", "stripe-dual-parity", "stripe-dual-parity-stripe", "stripe-parity", "stripe-parity-stripe", "unspecified"], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("StorageVirtualDrive", "storageVirtualDrive", "vd-[Id]", _VersionMeta.Version211a, "InputOutput", 0x3fL, [], [u'faultInst', u'storageLunDisk', u'storageOperation'], [None], ["read-only"])
}

