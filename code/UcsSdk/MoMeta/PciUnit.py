import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PciUnit(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PciUnit")

	@staticmethod
	def ClassId():
		return "pciUnit"

	DN = "Dn"
	ID = "Id"
	LOCATION_DN = "LocationDn"
	MODEL = "Model"
	OPER_QUALIFIER_REASON = "OperQualifierReason"
	OPER_STATE = "OperState"
	OPERABILITY = "Operability"
	PCI_ADDR = "PciAddr"
	PCI_SLOT = "PciSlot"
	PERF = "Perf"
	POWER = "Power"
	PRESENCE = "Presence"
	REVISION = "Revision"
	RN = "Rn"
	SERIAL = "Serial"
	STATUS = "Status"
	THERMAL = "Thermal"
	VENDOR = "Vendor"
	VOLTAGE = "Voltage"

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
	CONST_THERMAL_LOWER_CRITICAL = "lower-critical"
	CONST_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
	CONST_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
	CONST_THERMAL_NOT_SUPPORTED = "not-supported"
	CONST_THERMAL_OK = "ok"
	CONST_THERMAL_UNKNOWN = "unknown"
	CONST_THERMAL_UPPER_CRITICAL = "upper-critical"
	CONST_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
	CONST_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
	CONST_VOLTAGE_LOWER_CRITICAL = "lower-critical"
	CONST_VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
	CONST_VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
	CONST_VOLTAGE_NOT_SUPPORTED = "not-supported"
	CONST_VOLTAGE_OK = "ok"
	CONST_VOLTAGE_UNKNOWN = "unknown"
	CONST_VOLTAGE_UPPER_CRITICAL = "upper-critical"
	CONST_VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
	CONST_VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
