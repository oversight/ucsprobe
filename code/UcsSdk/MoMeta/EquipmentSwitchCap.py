import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentSwitchCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentSwitchCap")

	@staticmethod
	def ClassId():
		return "equipmentSwitchCap"

	DESCR = "Descr"
	DN = "Dn"
	FAN_MODULES_SUPPORTED = "FanModulesSupported"
	LOCATOR_BEACON_SUPPORTED = "LocatorBeaconSupported"
	MAX_ACTIVE_SPAN_SESSION_COUNT = "MaxActiveSpanSessionCount"
	MAX_ETH1G_PORT = "MaxEth1gPort"
	MAX_ETH1G_SLOT = "MaxEth1gSlot"
	MAX_ETH_PC_MEMBERS = "MaxEthPcMembers"
	MAX_ETH_PCS = "MaxEthPcs"
	MAX_FCOE_PC_MEMBERS = "MaxFcoePcMembers"
	MAX_UPLINK_PORTS = "MaxUplinkPorts"
	MGMT_DAUGHTER_CARD_SLOT_ID = "MgmtDaughterCardSlotId"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SERENO_NETFLOW_SUPPORTED = "SerenoNetflowSupported"
	STATUS = "Status"

	CONST_FAN_MODULES_SUPPORTED_FALSE = "false"
	CONST_FAN_MODULES_SUPPORTED_NO = "no"
	CONST_FAN_MODULES_SUPPORTED_TRUE = "true"
	CONST_FAN_MODULES_SUPPORTED_YES = "yes"
	CONST_INT_ID_NONE = "none"
	CONST_LOCATOR_BEACON_SUPPORTED_FALSE = "false"
	CONST_LOCATOR_BEACON_SUPPORTED_NO = "no"
	CONST_LOCATOR_BEACON_SUPPORTED_TRUE = "true"
	CONST_LOCATOR_BEACON_SUPPORTED_YES = "yes"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SERENO_NETFLOW_SUPPORTED_FALSE = "false"
	CONST_SERENO_NETFLOW_SUPPORTED_NO = "no"
	CONST_SERENO_NETFLOW_SUPPORTED_TRUE = "true"
	CONST_SERENO_NETFLOW_SUPPORTED_YES = "yes"
