import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageConnectionPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageConnectionPolicy")

	@staticmethod
	def ClassId():
		return "storageConnectionPolicy"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	OPER_STATE = "OperState"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	ZONING_TYPE = "ZoningType"

	CONST_INT_ID_NONE = "none"
	CONST_OPER_STATE_MISCONFIGURED = "misconfigured"
	CONST_OPER_STATE_OK = "ok"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_ZONING_TYPE_NONE = "none"
	CONST_ZONING_TYPE_SIMT = "simt"
	CONST_ZONING_TYPE_SIST = "sist"
