import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsmaintMaintPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsmaintMaintPolicy")

	@staticmethod
	def ClassId():
		return "lsmaintMaintPolicy"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	OPER_SCHED_NAME = "OperSchedName"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SCHED_NAME = "SchedName"
	STATUS = "Status"
	UPTIME_DISR = "UptimeDisr"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_UPTIME_DISR_IMMEDIATE = "immediate"
	CONST_UPTIME_DISR_TIMER_AUTOMATIC = "timer-automatic"
	CONST_UPTIME_DISR_USER_ACK = "user-ack"
