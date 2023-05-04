import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CimcvmediaMountConfigPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CimcvmediaMountConfigPolicy")

	@staticmethod
	def ClassId():
		return "cimcvmediaMountConfigPolicy"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RETRY_ON_MOUNT_FAIL = "RetryOnMountFail"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_RETRY_ON_MOUNT_FAIL_NO = "no"
	CONST_RETRY_ON_MOUNT_FAIL_YES = "yes"
