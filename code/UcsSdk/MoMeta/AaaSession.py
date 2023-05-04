import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaSession(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaSession")

	@staticmethod
	def ClassId():
		return "aaaSession"

	DN = "Dn"
	HOST = "Host"
	ID = "Id"
	INT_DEL = "IntDel"
	LOGIN_TIME = "LoginTime"
	PID = "Pid"
	REFRESH_PERIOD = "RefreshPeriod"
	RN = "Rn"
	SESSION_TIMEOUT = "SessionTimeout"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TERM = "Term"
	UI = "Ui"
	USER = "User"

	CONST_INT_DEL_FALSE = "false"
	CONST_INT_DEL_NO = "no"
	CONST_INT_DEL_TRUE = "true"
	CONST_INT_DEL_YES = "yes"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_UI_EP = "ep"
	CONST_UI_KVM = "kvm"
	CONST_UI_NONE = "none"
	CONST_UI_SHELL = "shell"
	CONST_UI_SOL = "sol"
	CONST_UI_VMEDIA = "vmedia"
	CONST_UI_WEB = "web"
