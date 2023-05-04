import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EventPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EventPolicy")

	@staticmethod
	def ClassId():
		return "eventPolicy"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RETENTION_INTERVAL = "RetentionInterval"
	RN = "Rn"
	SIZE_LIMIT = "SizeLimit"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_RETENTION_INTERVAL_FOREVER = "forever"
	CONST_SIZE_LIMIT_MAX = "max"
