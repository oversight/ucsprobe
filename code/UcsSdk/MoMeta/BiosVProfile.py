import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BiosVProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"BiosVProfile")

	@staticmethod
	def ClassId():
		return "biosVProfile"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	REBOOT_ON_UPDATE = "RebootOnUpdate"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_REBOOT_ON_UPDATE_FALSE = "false"
	CONST_REBOOT_ON_UPDATE_NO = "no"
	CONST_REBOOT_ON_UPDATE_TRUE = "true"
	CONST_REBOOT_ON_UPDATE_YES = "yes"
