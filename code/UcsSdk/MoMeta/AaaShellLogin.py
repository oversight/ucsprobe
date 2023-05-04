import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaShellLogin(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaShellLogin")

	@staticmethod
	def ClassId():
		return "aaaShellLogin"

	DESCR = "Descr"
	DN = "Dn"
	ID = "Id"
	LOCAL_HOST = "LocalHost"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	REMOTE_HOST = "RemoteHost"
	RN = "Rn"
	SESSION = "Session"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SESSION_IPMI = "ipmi"
	CONST_SESSION_LOCAL = "local"
	CONST_SESSION_REMOTE = "remote"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
