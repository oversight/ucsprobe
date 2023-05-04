import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageFlexFlashController(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageFlexFlashController")

	@staticmethod
	def ClassId():
		return "storageFlexFlashController"

	CONTROLLER_HEALTH = "ControllerHealth"
	CONTROLLER_STATE = "ControllerState"
	DN = "Dn"
	FLEX_FLASH_TYPE = "FlexFlashType"
	ID = "Id"
	LOCATION_DN = "LocationDn"
	MODEL = "Model"
	OPER_QUALIFIER_REASON = "OperQualifierReason"
	OPER_STATE = "OperState"
	OPERABILITY = "Operability"
	PCI_ADDR = "PciAddr"
	PCI_SLOT = "PciSlot"
	PERF = "Perf"
	PHYSICAL_DRIVE_COUNT = "PhysicalDriveCount"
	POWER = "Power"
	PRESENCE = "Presence"
	PRIMARY_SLOT_NUMBER = "PrimarySlotNumber"
	RAID_SYNC_SUPPORT = "RaidSyncSupport"
	READ_ERROR_THRESHOLD = "ReadErrorThreshold"
	REVISION = "Revision"
	RN = "Rn"
	SERIAL = "Serial"
	STATUS = "Status"
	THERMAL = "Thermal"
	TYPE = "Type"
	VENDOR = "Vendor"
	VIRTUAL_DRIVE_COUNT = "VirtualDriveCount"
	VOLTAGE = "Voltage"
	WRITE_ERROR_THRESHOLD = "WriteErrorThreshold"

	CONST_CONTROLLER_HEALTH_FFCH_ERROR_CARDS_ACCESS_ERROR = "FFCH_ERROR_CARDS_ACCESS_ERROR"
	CONST_CONTROLLER_HEALTH_FFCH_ERROR_CARD_SIZE_MISMATCH = "FFCH_ERROR_CARD_SIZE_MISMATCH"
	CONST_CONTROLLER_HEALTH_FFCH_ERROR_INCONSISTANT_METADATA_IGNORED = "FFCH_ERROR_INCONSISTANT_METADATA_IGNORED"
	CONST_CONTROLLER_HEALTH_FFCH_ERROR_INVALID_SIZE = "FFCH_ERROR_INVALID_SIZE"
	CONST_CONTROLLER_HEALTH_FFCH_ERROR_MEDIA_WRITE_PROTECTED = "FFCH_ERROR_MEDIA_WRITE_PROTECTED"
	CONST_CONTROLLER_HEALTH_FFCH_ERROR_OLD_FIRMWARE_RUNNING = "FFCH_ERROR_OLD_FIRMWARE_RUNNING"
	CONST_CONTROLLER_HEALTH_FFCH_ERROR_REBOOTED_DURING_REBUILD = "FFCH_ERROR_REBOOTED_DURING_REBUILD"
	CONST_CONTROLLER_HEALTH_FFCH_ERROR_SD247_CARD_DETECTED = "FFCH_ERROR_SD247_CARD_DETECTED"
	CONST_CONTROLLER_HEALTH_FFCH_ERROR_SD253_WITH_UN_OR_SD247 = "FFCH_ERROR_SD253_WITH_UN_OR_SD247"
	CONST_CONTROLLER_HEALTH_FFCH_ERROR_SD_CARD_NOT_CONFIGURED = "FFCH_ERROR_SD_CARD_NOT_CONFIGURED"
	CONST_CONTROLLER_HEALTH_FFCH_ERROR_SECONDARY_UNHEALTHY_CARD = "FFCH_ERROR_SECONDARY_UNHEALTHY_CARD"
	CONST_CONTROLLER_HEALTH_FFCH_INCONSISTENT_METADATA = "FFCH_INCONSISTENT_METADATA"
	CONST_CONTROLLER_HEALTH_FFCH_METADATA_FAILURE = "FFCH_METADATA_FAILURE"
	CONST_CONTROLLER_HEALTH_FFCH_OK = "FFCH_OK"
	CONST_CONTROLLER_STATE_FFC_CONFIG = "FFC_CONFIG"
	CONST_CONTROLLER_STATE_FFC_FAILED = "FFC_FAILED"
	CONST_CONTROLLER_STATE_FFC_INIT = "FFC_INIT"
	CONST_CONTROLLER_STATE_FFC_REBUILDING = "FFC_REBUILDING"
	CONST_CONTROLLER_STATE_FFC_SOFTWARE_ERR = "FFC_SOFTWARE_ERR"
	CONST_CONTROLLER_STATE_FFC_UNINITALIZED = "FFC_UNINITALIZED"
	CONST_CONTROLLER_STATE_FFC_USB_CONNECTED = "FFC_USB_CONNECTED"
	CONST_CONTROLLER_STATE_FFC_USB_CONNECTING = "FFC_USB_CONNECTING"
	CONST_CONTROLLER_STATE_FFC_USB_DISCONNECTED = "FFC_USB_DISCONNECTED"
	CONST_CONTROLLER_STATE_FFC_USB_DISCONNECTING = "FFC_USB_DISCONNECTING"
	CONST_CONTROLLER_STATE_FFC_WAIT_USER = "FFC_WAIT_USER"
	CONST_FLEX_FLASH_TYPE_ASTORIA = "Astoria"
	CONST_FLEX_FLASH_TYPE_UNKNOWN = "Unknown"
	CONST_OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
	CONST_OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
	CONST_OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
	CONST_OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
	CONST_OPER_STATE_CONFIG = "config"
	CONST_OPER_STATE_DECOMISSIONING = "decomissioning"
	CONST_OPER_STATE_DEGRADED = "degraded"
	CONST_OPER_STATE_DISABLED = "disabled"
	CONST_OPER_STATE_DISCOVERY = "discovery"
	CONST_OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
	CONST_OPER_STATE_EQUIPMENT_PROBLEM = "equipment-problem"
	CONST_OPER_STATE_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
	CONST_OPER_STATE_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
	CONST_OPER_STATE_IDENTIFY = "identify"
	CONST_OPER_STATE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
	CONST_OPER_STATE_INOPERABLE = "inoperable"
	CONST_OPER_STATE_LINK_ACTIVATE_BLOCKED = "link-activate-blocked"
	CONST_OPER_STATE_MALFORMED_FRU = "malformed-fru"
	CONST_OPER_STATE_NOT_SUPPORTED = "not-supported"
	CONST_OPER_STATE_OPERABLE = "operable"
	CONST_OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
	CONST_OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
	CONST_OPER_STATE_POST_FAILURE = "post-failure"
	CONST_OPER_STATE_POWER_PROBLEM = "power-problem"
	CONST_OPER_STATE_POWERED_OFF = "powered-off"
	CONST_OPER_STATE_REMOVED = "removed"
	CONST_OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
	CONST_OPER_STATE_UNKNOWN = "unknown"
	CONST_OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
	CONST_OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
	CONST_OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
	CONST_OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
	CONST_OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
	CONST_OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
	CONST_OPERABILITY_CONFIG = "config"
	CONST_OPERABILITY_DECOMISSIONING = "decomissioning"
	CONST_OPERABILITY_DEGRADED = "degraded"
	CONST_OPERABILITY_DISABLED = "disabled"
	CONST_OPERABILITY_DISCOVERY = "discovery"
	CONST_OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
	CONST_OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
	CONST_OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
	CONST_OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
	CONST_OPERABILITY_IDENTIFY = "identify"
	CONST_OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
	CONST_OPERABILITY_INOPERABLE = "inoperable"
	CONST_OPERABILITY_LINK_ACTIVATE_BLOCKED = "link-activate-blocked"
	CONST_OPERABILITY_MALFORMED_FRU = "malformed-fru"
	CONST_OPERABILITY_NOT_SUPPORTED = "not-supported"
	CONST_OPERABILITY_OPERABLE = "operable"
	CONST_OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
	CONST_OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
	CONST_OPERABILITY_POST_FAILURE = "post-failure"
	CONST_OPERABILITY_POWER_PROBLEM = "power-problem"
	CONST_OPERABILITY_POWERED_OFF = "powered-off"
	CONST_OPERABILITY_REMOVED = "removed"
	CONST_OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
	CONST_OPERABILITY_UNKNOWN = "unknown"
	CONST_OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
	CONST_OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
	CONST_PERF_LOWER_CRITICAL = "lower-critical"
	CONST_PERF_LOWER_NON_CRITICAL = "lower-non-critical"
	CONST_PERF_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
	CONST_PERF_NOT_SUPPORTED = "not-supported"
	CONST_PERF_OK = "ok"
	CONST_PERF_UNKNOWN = "unknown"
	CONST_PERF_UPPER_CRITICAL = "upper-critical"
	CONST_PERF_UPPER_NON_CRITICAL = "upper-non-critical"
	CONST_PERF_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
	CONST_POWER_DEGRADED = "degraded"
	CONST_POWER_ERROR = "error"
	CONST_POWER_FAILED = "failed"
	CONST_POWER_NOT_SUPPORTED = "not-supported"
	CONST_POWER_OFF = "off"
	CONST_POWER_OFFDUTY = "offduty"
	CONST_POWER_OFFLINE = "offline"
	CONST_POWER_OK = "ok"
	CONST_POWER_ON = "on"
	CONST_POWER_ONLINE = "online"
	CONST_POWER_POWER_SAVE = "power-save"
	CONST_POWER_TEST = "test"
	CONST_POWER_UNKNOWN = "unknown"
	CONST_PRESENCE_EMPTY = "empty"
	CONST_PRESENCE_EQUIPPED = "equipped"
	CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
	CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
	CONST_PRESENCE_EQUIPPED_SLAVE = "equipped-slave"
	CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
	CONST_PRESENCE_INACCESSIBLE = "inaccessible"
	CONST_PRESENCE_MISMATCH = "mismatch"
	CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
	CONST_PRESENCE_MISMATCH_SLAVE = "mismatch-slave"
	CONST_PRESENCE_MISSING = "missing"
	CONST_PRESENCE_MISSING_SLAVE = "missing-slave"
	CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
	CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
	CONST_PRESENCE_UNKNOWN = "unknown"
	CONST_RAID_SYNC_SUPPORT_NO = "no"
	CONST_RAID_SYNC_SUPPORT_YES = "yes"
	CONST_THERMAL_LOWER_CRITICAL = "lower-critical"
	CONST_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
	CONST_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
	CONST_THERMAL_NOT_SUPPORTED = "not-supported"
	CONST_THERMAL_OK = "ok"
	CONST_THERMAL_UNKNOWN = "unknown"
	CONST_THERMAL_UPPER_CRITICAL = "upper-critical"
	CONST_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
	CONST_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
	CONST_TYPE_FLASH = "FLASH"
	CONST_TYPE_SAS = "SAS"
	CONST_TYPE_SATA = "SATA"
	CONST_TYPE_SD = "SD"
	CONST_TYPE_UNKNOWN = "unknown"
	CONST_VOLTAGE_LOWER_CRITICAL = "lower-critical"
	CONST_VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
	CONST_VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
	CONST_VOLTAGE_NOT_SUPPORTED = "not-supported"
	CONST_VOLTAGE_OK = "ok"
	CONST_VOLTAGE_UNKNOWN = "unknown"
	CONST_VOLTAGE_UPPER_CRITICAL = "upper-critical"
	CONST_VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
	CONST_VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"