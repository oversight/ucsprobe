import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageAuthKey(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageAuthKey")

	@staticmethod
	def ClassId():
		return "storageAuthKey"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	PASSWORD = "Password"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"
	USER_ID = "UserId"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_TYPE_INITIATOR = "initiator"
	CONST_TYPE_TARGET = "target"
