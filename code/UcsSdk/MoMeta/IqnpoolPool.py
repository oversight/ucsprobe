import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IqnpoolPool(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IqnpoolPool")

	@staticmethod
	def ClassId():
		return "iqnpoolPool"

	ASSIGNED = "Assigned"
	ASSIGNMENT_ORDER = "AssignmentOrder"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PREFIX = "Prefix"
	RN = "Rn"
	SIZE = "Size"
	STATUS = "Status"

	CONST_ASSIGNMENT_ORDER_DEFAULT = "default"
	CONST_ASSIGNMENT_ORDER_SEQUENTIAL = "sequential"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
