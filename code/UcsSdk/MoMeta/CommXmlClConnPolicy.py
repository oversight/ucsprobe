import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommXmlClConnPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommXmlClConnPolicy")

	@staticmethod
	def ClassId():
		return "commXmlClConnPolicy"

	ADMIN_STATE = "AdminState"
	CLIENT_TYPE = "ClientType"
	DESCR = "Descr"
	DN = "Dn"
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
	CONST_CLIENT_TYPE_EXTRENAL_API_CLIENT = "extrenal-api-client"
	CONST_CLIENT_TYPE_FLEX_UI = "flex-ui"
	CONST_CLIENT_TYPE_JAVA_UI = "java-ui"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PROTO_ALL = "all"
	CONST_PROTO_NONE = "none"
	CONST_PROTO_TCP = "tcp"
	CONST_PROTO_UDP = "udp"
