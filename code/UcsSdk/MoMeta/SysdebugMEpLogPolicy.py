import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SysdebugMEpLogPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SysdebugMEpLogPolicy")

	@staticmethod
	def ClassId():
		return "sysdebugMEpLogPolicy"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_TYPE_OBFL = "OBFL"
	CONST_TYPE_SEL = "SEL"
	CONST_TYPE_SYSLOG = "Syslog"
