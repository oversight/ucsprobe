import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareUpdatable(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareUpdatable")

	@staticmethod
	def ClassId():
		return "firmwareUpdatable"

	ADMIN_STATE = "AdminState"
	DEPLOYMENT = "Deployment"
	DN = "Dn"
	OPER_STATE = "OperState"
	OPER_STATE_QUAL = "OperStateQual"
	PREV_VERSION = "PrevVersion"
	RN = "Rn"
	STATUS = "Status"
	VERSION = "Version"

	CONST_ADMIN_STATE_TRIGGER = "trigger"
	CONST_ADMIN_STATE_TRIGGERED = "triggered"
	CONST_DEPLOYMENT_BACKUP = "backup"
	CONST_DEPLOYMENT_UNSPECIFIED = "unspecified"
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
	CONST_OPER_STATE_QUAL_BOOT_CONF_MISSING = "boot-conf-missing"
	CONST_OPER_STATE_QUAL_CHECKSUM_FAILURE = "checksum-failure"
	CONST_OPER_STATE_QUAL_CRC_FAILURE = "crc-failure"
	CONST_OPER_STATE_QUAL_FILESYSTEM_ERROR = "filesystem-error"
	CONST_OPER_STATE_QUAL_MGMT_CONNECT_ERROR = "mgmt-connect-error"
	CONST_OPER_STATE_QUAL_NONE = "none"
	CONST_OPER_STATE_QUAL_UNKNOWN_ERROR = "unknown-error"
