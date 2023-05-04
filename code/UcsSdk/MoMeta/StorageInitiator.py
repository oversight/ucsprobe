import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageInitiator(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageInitiator")

	@staticmethod
	def ClassId():
		return "storageInitiator"

	DESCR = "Descr"
	DN = "Dn"
	DUPLICATE_TARGET = "DuplicateTarget"
	NAME = "Name"
	OPER_STATE = "OperState"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_OPER_STATE_MISCONFIGURED = "misconfigured"
	CONST_OPER_STATE_OK = "ok"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
