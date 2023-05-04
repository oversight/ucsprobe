import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricFlowMonDefinition(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricFlowMonDefinition")

	@staticmethod
	def ClassId():
		return "fabricFlowMonDefinition"

	DESCR = "Descr"
	DN = "Dn"
	IPV4KEYS = "Ipv4keys"
	IPV6KEYS = "Ipv6keys"
	KEY_TYPE = "KeyType"
	L2KEYS = "L2keys"
	NAME = "Name"
	NONKEYS = "Nonkeys"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RECORD_TYPE = "RecordType"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_KEY_TYPE_IPV4KEYS = "ipv4keys"
	CONST_KEY_TYPE_IPV6KEYS = "ipv6keys"
	CONST_KEY_TYPE_L2KEYS = "l2keys"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_RECORD_TYPE_SYSTEM_DEFINED = "system-defined"
	CONST_RECORD_TYPE_USER_DEFINED = "user-defined"
