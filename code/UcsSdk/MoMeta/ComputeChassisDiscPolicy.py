import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeChassisDiscPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeChassisDiscPolicy")

	@staticmethod
	def ClassId():
		return "computeChassisDiscPolicy"

	ACTION = "Action"
	DESCR = "Descr"
	DN = "Dn"
	LINK_AGGREGATION_PREF = "LinkAggregationPref"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	QUALIFIER = "Qualifier"
	REBALANCE = "Rebalance"
	RN = "Rn"
	STATUS = "Status"

	CONST_ACTION_1_LINK = "1-link"
	CONST_ACTION_2_LINK = "2-link"
	CONST_ACTION_4_LINK = "4-link"
	CONST_ACTION_8_LINK = "8-link"
	CONST_ACTION_IMMEDIATE = "immediate"
	CONST_ACTION_PLATFORM_MAX = "platform-max"
	CONST_ACTION_USER_ACKNOWLEDGED = "user-acknowledged"
	CONST_INT_ID_NONE = "none"
	CONST_LINK_AGGREGATION_PREF_NONE = "none"
	CONST_LINK_AGGREGATION_PREF_PORT_CHANNEL = "port-channel"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_REBALANCE_IMMEDIATE = "immediate"
	CONST_REBALANCE_USER_ACKNOWLEDGED = "user-acknowledged"
