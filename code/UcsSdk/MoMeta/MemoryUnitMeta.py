import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"AdminState":UcsPropertyMeta("AdminState", "adminState", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadWrite, 0x1L, None, None, None, ["policy", "reset-errors"], ["0-4294967295"]),
	"Array":UcsPropertyMeta("Array", "array", "ushort", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Bank":UcsPropertyMeta("Bank", "bank", "ushort", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Capacity":UcsPropertyMeta("Capacity", "capacity", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unspecified"], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version101e, UcsPropertyMeta.Internal, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"Clock":UcsPropertyMeta("Clock", "clock", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unspecified"], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x4L, 0, 256, None, [], ["0-4294967295"]),
	"FormFactor":UcsPropertyMeta("FormFactor", "formFactor", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["DIMM", "FB-DIMM", "Other", "RIMM", "SIMM", "SODIMM", "SRIMM", "TSOP", "Unknown", "undiscovered"], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "uint", _VersionMeta.Version101e, UcsPropertyMeta.Naming, 0x8L, None, None, None, [], ["1-256"]),
	"Latency":UcsPropertyMeta("Latency", "latency", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unspecified"], ["0-4294967295"]),
	"Location":UcsPropertyMeta("Location", "location", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"LocationDn":UcsPropertyMeta("LocationDn", "locationDn", "string", _VersionMeta.Version222c, UcsPropertyMeta.ReadOnly, None, 0, 256, None, [], ["0-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"OperQualifier":UcsPropertyMeta("OperQualifier", "operQualifier", "string", _VersionMeta.Version141i, UcsPropertyMeta.ReadOnly, None, None, None, """((defaultValue|none|uncorrectable-ecc-error|correctable-ecc-error|address-parity-error|memory-mismatch-error),){0,5}(defaultValue|none|uncorrectable-ecc-error|correctable-ecc-error|address-parity-error|memory-mismatch-error){0,1}""", [], ["0-4294967295"]),
	"OperQualifierReason":UcsPropertyMeta("OperQualifierReason", "operQualifierReason", "string", _VersionMeta.Version211a, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"OperState":UcsPropertyMeta("OperState", "operState", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
	"Operability":UcsPropertyMeta("Operability", "operability", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
	"Perf":UcsPropertyMeta("Perf", "perf", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
	"Power":UcsPropertyMeta("Power", "power", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], ["0-4294967295"]),
	"Presence":UcsPropertyMeta("Presence", "presence", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
	"Revision":UcsPropertyMeta("Revision", "revision", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, 0x10L, 0, 256, None, [], ["0-4294967295"]),
	"Serial":UcsPropertyMeta("Serial", "serial", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Set":UcsPropertyMeta("Set", "set", "byte", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Speed":UcsPropertyMeta("Speed", "speed", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unspecified"], ["0-4294967295"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Thermal":UcsPropertyMeta("Thermal", "thermal", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
	"Type":UcsPropertyMeta("Type", "type", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["3DRAM", "CDRAM", "DDR", "DDR2", "DDR2 FB-DIMM", "DDR3", "DRAM", "EDRAM", "EEPROM", "EPROM", "FBD2", "FEPROM", "FLASH", "Other", "RAM", "RDRAM", "ROM", "SDRAM", "SGRAM", "SRAM", "Unknown", "VRAM", "undiscovered"], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Visibility":UcsPropertyMeta("Visibility", "visibility", "string", _VersionMeta.Version102d, UcsPropertyMeta.ReadOnly, None, None, None, None, ["no", "unknown", "yes"], ["0-4294967295"]),
	"Voltage":UcsPropertyMeta("Voltage", "voltage", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
	"Width":UcsPropertyMeta("Width", "width", "string", _VersionMeta.Version101e, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unspecified"], ["0-4294967295"]),
	"Meta":UcsMoMeta("MemoryUnit", "memoryUnit", "mem-[Id]", _VersionMeta.Version101e, "InputOutput", 0x3fL, [], [u'faultInst', u'memoryErrorStats', u'memoryUnitEnvStats'], ["Get"], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"])
}

