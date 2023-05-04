import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareStatus(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareStatus")

	@staticmethod
	def ClassId():
		return "firmwareStatus"

	CIMC_VERSION = "CimcVersion"
	DN = "Dn"
	FIRMWARE_STATE = "FirmwareState"
	OPER_STATE = "OperState"
	PACKAGE_VERSION = "PackageVersion"
	PLD_VERSION = "PldVersion"
	RN = "Rn"
	STATUS = "Status"

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
