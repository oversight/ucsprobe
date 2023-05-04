import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ControllerStatus":UcsPropertyMeta("ControllerStatus", "controllerStatus", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["failed", "optimal", "unknown", "unresponsive"], ["0-4294967295"]),
	"DeviceRaidSupport":UcsPropertyMeta("DeviceRaidSupport", "deviceRaidSupport", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"FaultMonitoring":UcsPropertyMeta("FaultMonitoring", "faultMonitoring", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, None, None, None, ["notSupported", "supported"], ["0-4294967295"]),
	"HwRevision":UcsPropertyMeta("HwRevision", "hwRevision", "string", _VersionMeta.Version201m, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "uint", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x4L, None, None, None, [], ["1-64"]),
	"Lc":UcsPropertyMeta("Lc", "lc", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], ["0-4294967295"]),
	"LocationDn":UcsPropertyMeta("LocationDn", "locationDn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"OobControllerId":UcsPropertyMeta("OobControllerId", "oobControllerId", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["not-applicable"], ["0-4294967295"]),
	"OobInterfaceSupported":UcsPropertyMeta("OobInterfaceSupported", "oobInterfaceSupported", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
	"OperQualifierReason":UcsPropertyMeta("OperQualifierReason", "operQualifierReason", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
	"Operability":UcsPropertyMeta("Operability", "operability", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
	"PciAddr":UcsPropertyMeta("PciAddr", "pciAddr", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"PciSlot":UcsPropertyMeta("PciSlot", "pciSlot", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Perf":UcsPropertyMeta("Perf", "perf", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
	"Power":UcsPropertyMeta("Power", "power", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], ["0-4294967295"]),
	"Presence":UcsPropertyMeta("Presence", "presence", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
	"RaidSupport":UcsPropertyMeta("RaidSupport", "raidSupport", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"RebuildRate":UcsPropertyMeta("RebuildRate", "rebuildRate", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unknown"], ["0-101"]),
	"Revision":UcsPropertyMeta("Revision", "revision", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Serial":UcsPropertyMeta("Serial", "serial", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Thermal":UcsPropertyMeta("Thermal", "thermal", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x20L, None, None, None, ["FLASH", "SAS", "SATA", "SD", "unknown"], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Voltage":UcsPropertyMeta("Voltage", "voltage", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
	"Meta":UcsMoMeta("StorageController", "storageController", "storage-[Type]-[Id]", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [u'faultInst', u'firmwareBootDefinition', u'firmwareRunning', u'storageDrive', u'storageEnclosure', u'storageLocalDisk', u'storageLocalDiskConfigDef', u'storageLocalLun', u'storageMezzFlashLife', u'storageOperation', u'storageRaidBattery', u'storageVirtualDrive'], ["Get"], ["read-only"])
}

