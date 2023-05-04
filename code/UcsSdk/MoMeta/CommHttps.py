import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommHttps(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommHttps")

	@staticmethod
	def ClassId():
		return "commHttps"

	ADMIN_STATE = "AdminState"
	CIPHER_SUITE = "CipherSuite"
	CIPHER_SUITE_MODE = "CipherSuiteMode"
	DESCR = "Descr"
	DN = "Dn"
	KEY_RING = "KeyRing"
	NAME = "Name"
	OPER_PORT = "OperPort"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PORT = "Port"
	PROTO = "Proto"
	RN = "Rn"
	STATUS = "Status"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_CIPHER_SUITE_MODE_CUSTOM = "custom"
	CONST_CIPHER_SUITE_MODE_HIGH_STRENGTH = "high-strength"
	CONST_CIPHER_SUITE_MODE_LOW_STRENGTH = "low-strength"
	CONST_CIPHER_SUITE_MODE_MEDIUM_STRENGTH = "medium-strength"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PROTO_ALL = "all"
	CONST_PROTO_NONE = "none"
	CONST_PROTO_TCP = "tcp"
	CONST_PROTO_UDP = "udp"
