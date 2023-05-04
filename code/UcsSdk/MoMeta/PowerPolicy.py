import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PowerPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PowerPolicy")

	@staticmethod
	def ClassId():
		return "powerPolicy"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	OPER_PRIO = "OperPrio"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PRIO = "Prio"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_OPER_PRIO_NO_CAP = "no-cap"
	CONST_OPER_PRIO_UTILITY = "utility"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PRIO_NO_CAP = "no-cap"
	CONST_PRIO_UTILITY = "utility"
