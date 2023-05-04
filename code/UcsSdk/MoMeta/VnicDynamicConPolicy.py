import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicDynamicConPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicDynamicConPolicy")

	@staticmethod
	def ClassId():
		return "vnicDynamicConPolicy"

	ADAPTOR_PROFILE_NAME = "AdaptorProfileName"
	DESCR = "Descr"
	DN = "Dn"
	DYNAMIC_ETH = "DynamicEth"
	MTU = "Mtu"
	NAME = "Name"
	NAMING_PREFIX = "NamingPrefix"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PROTECTION = "Protection"
	RN = "Rn"
	STATUS = "Status"

	CONST_DYNAMIC_ETH_OFF = "off"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PROTECTION_NONE = "none"
	CONST_PROTECTION_PROTECTED = "protected"
	CONST_PROTECTION_PROTECTED_PREF_A = "protected-pref-a"
	CONST_PROTECTION_PROTECTED_PREF_B = "protected-pref-b"
