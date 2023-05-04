import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommSnmp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommSnmp")

	@staticmethod
	def ClassId():
		return "commSnmp"

	ADMIN_STATE = "AdminState"
	COMMUNITY = "Community"
	CONFIG_STATE = "ConfigState"
	DESCR = "Descr"
	DN = "Dn"
	IS_SET_SNMP_SECURE = "IsSetSnmpSecure"
	NAME = "Name"
	OPER_PORT = "OperPort"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PORT = "Port"
	PROTO = "Proto"
	RN = "Rn"
	STATUS = "Status"
	SYS_CONTACT = "SysContact"
	SYS_LOCATION = "SysLocation"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_CONFIG_STATE_NOT_APPLIED = "not-applied"
	CONST_CONFIG_STATE_OK = "ok"
	CONST_INT_ID_NONE = "none"
	CONST_IS_SET_SNMP_SECURE_FALSE = "false"
	CONST_IS_SET_SNMP_SECURE_NO = "no"
	CONST_IS_SET_SNMP_SECURE_TRUE = "true"
	CONST_IS_SET_SNMP_SECURE_YES = "yes"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PROTO_ALL = "all"
	CONST_PROTO_NONE = "none"
	CONST_PROTO_TCP = "tcp"
	CONST_PROTO_UDP = "udp"
