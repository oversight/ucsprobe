import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PowerGroup(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PowerGroup")

	@staticmethod
	def ClassId():
		return "powerGroup"

	ADMIN_COMMITTED = "AdminCommitted"
	ADMIN_PEAK = "AdminPeak"
	CUR_REQ_POWER = "CurReqPower"
	CURRENT_POWER = "CurrentPower"
	DESCR = "Descr"
	DN = "Dn"
	MIN_REQ_POWER = "MinReqPower"
	NAME = "Name"
	OPER_COMMITTED = "OperCommitted"
	OPER_PEAK = "OperPeak"
	OPER_STATE = "OperState"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	QUALIFIER = "Qualifier"
	REALLOC = "Realloc"
	RN = "Rn"
	STATUS = "Status"

	CONST_ADMIN_COMMITTED_UNBOUNDED = "unbounded"
	CONST_ADMIN_PEAK_UNBOUNDED = "unbounded"
	CONST_CUR_REQ_POWER_UNBOUNDED = "unbounded"
	CONST_CURRENT_POWER_UNBOUNDED = "unbounded"
	CONST_INT_ID_NONE = "none"
	CONST_MIN_REQ_POWER_UNBOUNDED = "unbounded"
	CONST_OPER_COMMITTED_UNBOUNDED = "unbounded"
	CONST_OPER_PEAK_UNBOUNDED = "unbounded"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_REALLOC_CHASSIS = "chassis"
	CONST_REALLOC_NONE = "none"
