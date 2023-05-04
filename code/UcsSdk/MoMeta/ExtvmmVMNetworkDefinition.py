import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtvmmVMNetworkDefinition(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtvmmVMNetworkDefinition")

	@staticmethod
	def ClassId():
		return "extvmmVMNetworkDefinition"

	DESCR = "Descr"
	DN = "Dn"
	EXT_IP_POOL_NAME = "ExtIpPoolName"
	GUID = "Guid"
	IP_POOL_GUID = "IpPoolGuid"
	MAX_PORTS = "MaxPorts"
	NAME = "Name"
	OPER_EXT_IP_POOL_NAME = "OperExtIpPoolName"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PRIMARY_VLAN_ID = "PrimaryVlanId"
	REF_OPER_STATE = "RefOperState"
	RN = "Rn"
	STATUS = "Status"
	VLAN_NAME = "VlanName"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_REF_OPER_STATE_INVALID_REFERENCE = "invalid-reference"
	CONST_REF_OPER_STATE_UP = "up"
