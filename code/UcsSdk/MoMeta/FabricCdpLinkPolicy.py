import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricCdpLinkPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricCdpLinkPolicy")

	@staticmethod
	def ClassId():
		return "fabricCdpLinkPolicy"

	ADMIN_STATE = "AdminState"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PROTOCOL = "Protocol"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PROTOCOL_CDP = "cdp"
	CONST_PROTOCOL_UDLD = "udld"
	CONST_PROTOCOL_UNKNOWN = "unknown"
