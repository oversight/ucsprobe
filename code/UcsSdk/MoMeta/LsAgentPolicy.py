import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsAgentPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsAgentPolicy")

	@staticmethod
	def ClassId():
		return "lsAgentPolicy"

	CAPABILITY = "Capability"
	DESCR = "Descr"
	DN = "Dn"
	MODE = "Mode"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_CAPABILITY_HOST_NAME_CONFIG = "host-name-config"
	CONST_CAPABILITY_L2_IF_CONFIG = "l2-if-config"
	CONST_CAPABILITY_L3_IF_CONFIG = "l3-if-config"
	CONST_CAPABILITY_STATES = "states"
	CONST_CAPABILITY_STATS = "stats"
	CONST_INT_ID_NONE = "none"
	CONST_MODE_FULL = "full"
	CONST_MODE_NO_AGENT = "no-agent"
	CONST_MODE_READ_ONLY = "read-only"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
