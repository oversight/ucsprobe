import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicFcGroupTempl(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicFcGroupTempl")

	@staticmethod
	def ClassId():
		return "vnicFcGroupTempl"

	ADAPTOR_PROFILE_NAME = "AdaptorProfileName"
	DESCR = "Descr"
	DN = "Dn"
	IDENT_POOL_NAME = "IdentPoolName"
	MAX_DATA_FIELD_SIZE = "MaxDataFieldSize"
	NAME = "Name"
	NW_TEMPL_NAME = "NwTemplName"
	OPER_STATS_POLICY_NAME = "OperStatsPolicyName"
	OPER_STORAGE_CONN_POLICY_NAME = "OperStorageConnPolicyName"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	QOS_POLICY_NAME = "QosPolicyName"
	RN = "Rn"
	STATS_POLICY_NAME = "StatsPolicyName"
	STATUS = "Status"
	STORAGE_CONN_POLICY_NAME = "StorageConnPolicyName"
	TEMPL_TYPE = "TemplType"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_TEMPL_TYPE_INITIAL_TEMPLATE = "initial-template"
	CONST_TEMPL_TYPE_UPDATING_TEMPLATE = "updating-template"
