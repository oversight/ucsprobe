import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtvmmFabricNetwork(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtvmmFabricNetwork")

	@staticmethod
	def ClassId():
		return "extvmmFabricNetwork"

	DESCR = "Descr"
	DN = "Dn"
	GUID = "Guid"
	NAME = "Name"
	NETWORK_TYPE = "NetworkType"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	REF_OPER_STATE = "RefOperState"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_NETWORK_TYPE_CONNECTED = "connected"
	CONST_NETWORK_TYPE_NOT_CONNECTED = "not-connected"
	CONST_NETWORK_TYPE_NOT_CONNECTED_PVLANS = "not-connected-pvlans"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_REF_OPER_STATE_INVALID_REFERENCE = "invalid-reference"
	CONST_REF_OPER_STATE_UP = "up"
