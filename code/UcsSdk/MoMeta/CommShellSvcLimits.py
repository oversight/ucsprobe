import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CommShellSvcLimits(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CommShellSvcLimits")

	@staticmethod
	def ClassId():
		return "commShellSvcLimits"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SESSIONS_PER_USER = "SessionsPerUser"
	STATUS = "Status"
	TOTAL_SESSIONS = "TotalSessions"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
