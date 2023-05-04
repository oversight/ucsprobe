import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricMulticastPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricMulticastPolicy")

	@staticmethod
	def ClassId():
		return "fabricMulticastPolicy"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	QUERIER_IP_ADDR = "QuerierIpAddr"
	QUERIER_STATE = "QuerierState"
	RN = "Rn"
	SNOOPING_STATE = "SnoopingState"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_QUERIER_STATE_DISABLED = "disabled"
	CONST_QUERIER_STATE_ENABLED = "enabled"
	CONST_SNOOPING_STATE_DISABLED = "disabled"
	CONST_SNOOPING_STATE_ENABLED = "enabled"
