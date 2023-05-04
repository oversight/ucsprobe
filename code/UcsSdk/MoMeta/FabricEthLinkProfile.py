import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricEthLinkProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricEthLinkProfile")

	@staticmethod
	def ClassId():
		return "fabricEthLinkProfile"

	CDP_LINK_POLICY_NAME = "CdpLinkPolicyName"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	OPER_CDP_LINK_POLICY_NAME = "OperCdpLinkPolicyName"
	OPER_UDLD_LINK_POLICY_NAME = "OperUdldLinkPolicyName"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	UDLD_LINK_POLICY_NAME = "UdldLinkPolicyName"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
