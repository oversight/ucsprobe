import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaEpAuthProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaEpAuthProfile")

	@staticmethod
	def ClassId():
		return "aaaEpAuthProfile"

	DESCR = "Descr"
	DN = "Dn"
	IPMI_OVER_LAN = "IpmiOverLan"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_IPMI_OVER_LAN_DISABLE = "disable"
	CONST_IPMI_OVER_LAN_ENABLE = "enable"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
