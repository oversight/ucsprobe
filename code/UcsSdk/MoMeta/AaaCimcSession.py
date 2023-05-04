import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaCimcSession(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaCimcSession")

	@staticmethod
	def ClassId():
		return "aaaCimcSession"

	ADMIN_STATE = "AdminState"
	CIMC_ADDR = "CimcAddr"
	DN = "Dn"
	ID = "Id"
	INT_DEL = "IntDel"
	IS_DELETE = "IsDelete"
	LAST_UPDATED_TIME = "LastUpdatedTime"
	LOGIN_TIME = "LoginTime"
	LS_DN = "LsDn"
	PID = "Pid"
	PN_DN = "PnDn"
	PRIV = "Priv"
	RN = "Rn"
	SOURCE_ADDR = "SourceAddr"
	STATUS = "Status"
	TYPE = "Type"
	USER = "User"

	CONST_ADMIN_STATE_ACTIVE = "active"
	CONST_ADMIN_STATE_INACTIVE = "inactive"
	CONST_INT_DEL_FALSE = "false"
	CONST_INT_DEL_NO = "no"
	CONST_INT_DEL_TRUE = "true"
	CONST_INT_DEL_YES = "yes"
	CONST_IS_DELETE_NO = "no"
	CONST_IS_DELETE_YES = "yes"
	CONST_TYPE_ALL = "all"
	CONST_TYPE_KVM = "kvm"
	CONST_TYPE_SOL = "sol"
	CONST_TYPE_VMEDIA = "vmedia"
