import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CallhomePolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CallhomePolicy")

	@staticmethod
	def ClassId():
		return "callhomePolicy"

	ADMIN_STATE = "AdminState"
	CAUSE = "Cause"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_CAUSE_ARP_TARGETS_CONFIG_ERROR = "arp-targets-config-error"
	CONST_CAUSE_ASSOCIATION_FAILED = "association-failed"
	CONST_CAUSE_CONFIGURATION_FAILURE = "configuration-failure"
	CONST_CAUSE_CONNECTIVITY_PROBLEM = "connectivity-problem"
	CONST_CAUSE_ELECTION_FAILURE = "election-failure"
	CONST_CAUSE_EQUIPMENT_DEGRADED = "equipment-degraded"
	CONST_CAUSE_EQUIPMENT_DISABLED = "equipment-disabled"
	CONST_CAUSE_EQUIPMENT_INACCESSIBLE = "equipment-inaccessible"
	CONST_CAUSE_EQUIPMENT_INOPERABLE = "equipment-inoperable"
	CONST_CAUSE_EQUIPMENT_OFFLINE = "equipment-offline"
	CONST_CAUSE_EQUIPMENT_PROBLEM = "equipment-problem"
	CONST_CAUSE_FRU_PROBLEM = "fru-problem"
	CONST_CAUSE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
	CONST_CAUSE_INVENTORY_FAILED = "inventory-failed"
	CONST_CAUSE_LICENSE_GRACEPERIOD_EXPIRED = "license-graceperiod-expired"
	CONST_CAUSE_LIMIT_REACHED = "limit-reached"
	CONST_CAUSE_LINK_DOWN = "link-down"
	CONST_CAUSE_MANAGEMENT_SERVICES_FAILURE = "management-services-failure"
	CONST_CAUSE_MANAGEMENT_SERVICES_UNRESPONSIVE = "management-services-unresponsive"
	CONST_CAUSE_MGMTIF_DOWN = "mgmtif-down"
	CONST_CAUSE_NDISC_TARGETS_CONFIG_ERROR = "ndisc-targets-config-error"
	CONST_CAUSE_PORT_FAILED = "port-failed"
	CONST_CAUSE_POWER_PROBLEM = "power-problem"
	CONST_CAUSE_THERMAL_PROBLEM = "thermal-problem"
	CONST_CAUSE_UNSPECIFIED = "unspecified"
	CONST_CAUSE_VERSION_INCOMPATIBLE = "version-incompatible"
	CONST_CAUSE_VIF_IDS_MISMATCH = "vif-ids-mismatch"
	CONST_CAUSE_VOLTAGE_PROBLEM = "voltage-problem"
