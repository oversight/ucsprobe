import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageIniGroup(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageIniGroup")

	@staticmethod
	def ClassId():
		return "storageIniGroup"

	DESCR = "Descr"
	DN = "Dn"
	GROUP_POLICY_NAME = "GroupPolicyName"
	NAME = "Name"
	OPER_PROTOCOL = "OperProtocol"
	OPER_STATE = "OperState"
	OWNER = "Owner"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_NAME = "PolicyName"
	POLICY_OWNER = "PolicyOwner"
	PROTOCOL = "Protocol"
	RMT_DISK_CFG_NAME = "RmtDiskCfgName"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_OPER_PROTOCOL_DERIVED = "derived"
	CONST_OPER_PROTOCOL_FC = "fc"
	CONST_OPER_PROTOCOL_ISCSI = "iscsi"
	CONST_OPER_STATE_MISCONFIGURED = "misconfigured"
	CONST_OPER_STATE_OK = "ok"
	CONST_OWNER_CONN_POLICY = "conn_policy"
	CONST_OWNER_LOGICAL = "logical"
	CONST_OWNER_PHYSICAL = "physical"
	CONST_OWNER_POLICY = "policy"
	CONST_OWNER_UNKNOWN = "unknown"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PROTOCOL_DERIVED = "derived"
	CONST_PROTOCOL_FC = "fc"
	CONST_PROTOCOL_ISCSI = "iscsi"
