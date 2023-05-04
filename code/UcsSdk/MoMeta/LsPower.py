import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsPower(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsPower")

	@staticmethod
	def ClassId():
		return "lsPower"

	DN = "Dn"
	RN = "Rn"
	STATE = "State"
	STATUS = "Status"

	CONST_STATE_ADMIN_DOWN = "admin-down"
	CONST_STATE_ADMIN_UP = "admin-up"
	CONST_STATE_BMC_RESET_IMMEDIATE = "bmc-reset-immediate"
	CONST_STATE_BMC_RESET_WAIT = "bmc-reset-wait"
	CONST_STATE_CMOS_RESET_IMMEDIATE = "cmos-reset-immediate"
	CONST_STATE_CYCLE_IMMEDIATE = "cycle-immediate"
	CONST_STATE_CYCLE_WAIT = "cycle-wait"
	CONST_STATE_DIAGNOSTIC_INTERRUPT = "diagnostic-interrupt"
	CONST_STATE_DOWN = "down"
	CONST_STATE_HARD_RESET_IMMEDIATE = "hard-reset-immediate"
	CONST_STATE_HARD_RESET_WAIT = "hard-reset-wait"
	CONST_STATE_IPMI_RESET = "ipmi-reset"
	CONST_STATE_KVM_RESET = "kvm-reset"
	CONST_STATE_SOFT_SHUT_DOWN = "soft-shut-down"
	CONST_STATE_SOFT_SHUT_DOWN_ONLY = "soft-shut-down-only"
	CONST_STATE_UP = "up"
