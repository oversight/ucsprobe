import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareBootUnit(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareBootUnit")

	@staticmethod
	def ClassId():
		return "firmwareBootUnit"

	ADMIN_STATE = "AdminState"
	DN = "Dn"
	IGNORE_COMP_CHECK = "IgnoreCompCheck"
	IMAGE = "Image"
	OPER_STATE = "OperState"
	PREV_VERSION = "PrevVersion"
	RESET_ON_ACTIVATE = "ResetOnActivate"
	RN = "Rn"
	SKIP_VALIDATION = "SkipValidation"
	STATUS = "Status"
	TYPE = "Type"
	VERSION = "Version"

	CONST_ADMIN_STATE_TRIGGER = "trigger"
	CONST_ADMIN_STATE_TRIGGERED = "triggered"
	CONST_IGNORE_COMP_CHECK_FALSE = "false"
	CONST_IGNORE_COMP_CHECK_NO = "no"
	CONST_IGNORE_COMP_CHECK_TRUE = "true"
	CONST_IGNORE_COMP_CHECK_YES = "yes"
	CONST_IMAGE_BACKUP = "backup"
	CONST_IMAGE_RUNNING = "running"
	CONST_OPER_STATE_ACTIVATING = "activating"
	CONST_OPER_STATE_AUTO_ACTIVATING = "auto-activating"
	CONST_OPER_STATE_AUTO_UPDATING = "auto-updating"
	CONST_OPER_STATE_BAD_IMAGE = "bad-image"
	CONST_OPER_STATE_FAILED = "failed"
	CONST_OPER_STATE_PENDING_NEXT_BOOT = "pending-next-boot"
	CONST_OPER_STATE_PENDING_POWER_CYCLE = "pending-power-cycle"
	CONST_OPER_STATE_READY = "ready"
	CONST_OPER_STATE_REBOOTING = "rebooting"
	CONST_OPER_STATE_SCHEDULED = "scheduled"
	CONST_OPER_STATE_SET_STARTUP = "set-startup"
	CONST_OPER_STATE_THROTTLED = "throttled"
	CONST_OPER_STATE_UPDATING = "updating"
	CONST_OPER_STATE_UPGRADING = "upgrading"
	CONST_RESET_ON_ACTIVATE_FALSE = "false"
	CONST_RESET_ON_ACTIVATE_NO = "no"
	CONST_RESET_ON_ACTIVATE_TRUE = "true"
	CONST_RESET_ON_ACTIVATE_YES = "yes"
	CONST_SKIP_VALIDATION_FALSE = "false"
	CONST_SKIP_VALIDATION_NO = "no"
	CONST_SKIP_VALIDATION_TRUE = "true"
	CONST_SKIP_VALIDATION_YES = "yes"
