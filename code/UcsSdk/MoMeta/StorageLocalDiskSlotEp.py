import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageLocalDiskSlotEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageLocalDiskSlotEp")

	@staticmethod
	def ClassId():
		return "storageLocalDiskSlotEp"

	CONFIGURATION = "Configuration"
	DN = "Dn"
	ID = "Id"
	OPER_QUALIFIER_REASON = "OperQualifierReason"
	OPERABILITY = "Operability"
	PEER_DN = "PeerDn"
	PRESENCE = "Presence"
	RN = "Rn"
	STATUS = "Status"

	CONST_CONFIGURATION_NOT_SUPPORTED = "not-supported"
	CONST_CONFIGURATION_SUPPORTED = "supported"
	CONST_CONFIGURATION_UNKNOWN = "unknown"
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
