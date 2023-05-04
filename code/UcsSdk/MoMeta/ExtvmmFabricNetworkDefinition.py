import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtvmmFabricNetworkDefinition(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtvmmFabricNetworkDefinition")

	@staticmethod
	def ClassId():
		return "extvmmFabricNetworkDefinition"

	ALLOWED_VNIC_TYPE = "AllowedVnicType"
	DESCR = "Descr"
	DN = "Dn"
	GUID = "Guid"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PRIMARY_VLAN_ID = "PrimaryVlanId"
	REF_OPER_STATE = "RefOperState"
	RN = "Rn"
	STATUS = "Status"

	CONST_ALLOWED_VNIC_TYPE_ETHER = "ether"
	CONST_ALLOWED_VNIC_TYPE_FC = "fc"
	CONST_ALLOWED_VNIC_TYPE_IPC = "ipc"
	CONST_ALLOWED_VNIC_TYPE_SCSI = "scsi"
	CONST_ALLOWED_VNIC_TYPE_UNKNOWN = "unknown"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_REF_OPER_STATE_INVALID_REFERENCE = "invalid-reference"
	CONST_REF_OPER_STATE_UP = "up"
