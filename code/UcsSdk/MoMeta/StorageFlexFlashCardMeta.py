import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsHandle import UcsVersion, UcsPropertyMeta, UcsMoMeta
from UcsMeta import _VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROPERTY_DICT = {
	"BlockSize":UcsPropertyMeta("BlockSize", "blockSize", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unknown"], ["0-4294967295"]),
	"CardHealth":UcsPropertyMeta("CardHealth", "cardHealth", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["FF_PHY_HEALTH_NA", "FF_PHY_HEALTH_OK", "FF_PHY_UNHEALTHY_OTHER", "FF_PHY_UNHEALTHY_RAID"], ["0-4294967295"]),
	"CardMode":UcsPropertyMeta("CardMode", "cardMode", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["FF_PHY_DRIVE_PRIMARY", "FF_PHY_DRIVE_SECONDARY_ACT", "FF_PHY_DRIVE_SECONDARY_UNHEALTHY", "FF_PHY_DRIVE_UNPAIRED_PRIMARY"], ["0-4294967295"]),
	"CardType":UcsPropertyMeta("CardType", "cardType", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"ChildAction":UcsPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.Version221b, UcsPropertyMeta.Internal, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], ["0-4294967295"]),
	"ConnectionProtocol":UcsPropertyMeta("ConnectionProtocol", "connectionProtocol", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["SAS", "SATA", "unspecified"], ["0-4294967295"]),
	"ControllerIndex":UcsPropertyMeta("ControllerIndex", "controllerIndex", "ushort", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Dn":UcsPropertyMeta("Dn", "dn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x2L, 0, 256, None, [], ["0-4294967295"]),
	"Id":UcsPropertyMeta("Id", "id", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x4L, None, None, None, [], ["0-4294967295"]),
	"MfgDate":UcsPropertyMeta("MfgDate", "mfgDate", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"MfgId":UcsPropertyMeta("MfgId", "mfgId", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Model":UcsPropertyMeta("Model", "model", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"NumberOfBlocks":UcsPropertyMeta("NumberOfBlocks", "numberOfBlocks", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unknown"], ["0-4294967295"]),
	"OemId":UcsPropertyMeta("OemId", "oemId", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"OperQualifierReason":UcsPropertyMeta("OperQualifierReason", "operQualifierReason", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
	"Operability":UcsPropertyMeta("Operability", "operability", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "link-activate-blocked", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
	"Presence":UcsPropertyMeta("Presence", "presence", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
	"ReadIOErrorCount":UcsPropertyMeta("ReadIOErrorCount", "readIOErrorCount", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Revision":UcsPropertyMeta("Revision", "revision", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Rn":UcsPropertyMeta("Rn", "rn", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, 0x8L, 0, 256, None, [], ["0-4294967295"]),
	"Serial":UcsPropertyMeta("Serial", "serial", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"Size":UcsPropertyMeta("Size", "size", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["unknown"], ["0-4294967295"]),
	"SlotNumber":UcsPropertyMeta("SlotNumber", "slotNumber", "ushort", _VersionMeta.Version221b, UcsPropertyMeta.Naming, 0x10L, None, None, None, [], ["1-64"]),
	"Status":UcsPropertyMeta("Status", "status", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadWrite, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
	"Vendor":UcsPropertyMeta("Vendor", "vendor", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, 0, 510, None, [], ["0-4294967295"]),
	"WriteEnable":UcsPropertyMeta("WriteEnable", "writeEnable", "string", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, ["no", "yes"], ["0-4294967295"]),
	"WriteIOErrorCount":UcsPropertyMeta("WriteIOErrorCount", "writeIOErrorCount", "uint", _VersionMeta.Version221b, UcsPropertyMeta.ReadOnly, None, None, None, None, [], ["0-4294967295"]),
	"Meta":UcsMoMeta("StorageFlexFlashCard", "storageFlexFlashCard", "card-[SlotNumber]", _VersionMeta.Version221b, "InputOutput", 0x3fL, [], [u'faultInst', u'storageFlexFlashDrive'], ["Get"], ["read-only"])
}

