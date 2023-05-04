import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VmVnicProfInst(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VmVnicProfInst")

	@staticmethod
	def ClassId():
		return "vmVnicProfInst"

	DESCR = "Descr"
	DN = "Dn"
	MAX_PORTS = "MaxPorts"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PROF_DN = "ProfDn"
	PROFILE_TYPE = "ProfileType"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PROFILE_TYPE_REGULAR = "regular"
	CONST_PROFILE_TYPE_SLA_ONLY = "sla-only"
