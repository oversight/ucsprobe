import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaUserData(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaUserData")

	@staticmethod
	def ClassId():
		return "aaaUserData"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PWD_CHANGE_COUNT = "PwdChangeCount"
	PWD_CHANGE_INTERVAL_BEGIN = "PwdChangeIntervalBegin"
	PWD_CHANGED_DATE = "PwdChangedDate"
	PWD_HISTORY = "PwdHistory"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
