import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaExtMgmtCutThruTkn(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaExtMgmtCutThruTkn")

	@staticmethod
	def ClassId():
		return "aaaExtMgmtCutThruTkn"

	AUTH_DOMAIN = "AuthDomain"
	AUTH_USER = "AuthUser"
	CREATION_TIME = "CreationTime"
	DESCR = "Descr"
	DN = "Dn"
	LOCALES = "Locales"
	NAME = "Name"
	PN_DN = "PnDn"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PRIV = "Priv"
	REMOTE = "Remote"
	RN = "Rn"
	STATUS = "Status"
	TOKEN = "Token"
	TYPE = "Type"
	USER = "User"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_REMOTE_FALSE = "false"
	CONST_REMOTE_NO = "no"
	CONST_REMOTE_TRUE = "true"
	CONST_REMOTE_YES = "yes"
	CONST_TYPE_KVM = "kvm"
