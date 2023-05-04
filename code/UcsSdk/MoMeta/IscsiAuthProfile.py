import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IscsiAuthProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IscsiAuthProfile")

	@staticmethod
	def ClassId():
		return "iscsiAuthProfile"

	CTPASSWORD = "Ctpassword"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	PASSWORD = "Password"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	USER_ID = "UserId"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
