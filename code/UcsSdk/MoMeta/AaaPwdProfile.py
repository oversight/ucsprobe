import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaPwdProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaPwdProfile")

	@staticmethod
	def ClassId():
		return "aaaPwdProfile"

	CHANGE_COUNT = "ChangeCount"
	CHANGE_DURING_INTERVAL = "ChangeDuringInterval"
	CHANGE_INTERVAL = "ChangeInterval"
	DESCR = "Descr"
	DN = "Dn"
	EXPIRATION_WARN_TIME = "ExpirationWarnTime"
	HISTORY_COUNT = "HistoryCount"
	NAME = "Name"
	NO_CHANGE_INTERVAL = "NoChangeInterval"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_CHANGE_DURING_INTERVAL_DISABLE = "disable"
	CONST_CHANGE_DURING_INTERVAL_ENABLE = "enable"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
