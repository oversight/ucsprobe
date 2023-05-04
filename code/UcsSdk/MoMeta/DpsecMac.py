import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DpsecMac(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DpsecMac")

	@staticmethod
	def ClassId():
		return "dpsecMac"

	DESCR = "Descr"
	DN = "Dn"
	FORGE = "Forge"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_FORGE_ALLOW = "allow"
	CONST_FORGE_DENY = "deny"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
