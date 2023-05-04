import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PowerBudget(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PowerBudget")

	@staticmethod
	def ClassId():
		return "powerBudget"

	ADMIN_COMMITTED = "AdminCommitted"
	ADMIN_PEAK = "AdminPeak"
	CAP_ACTION = "CapAction"
	CATALOG_POWER = "CatalogPower"
	CURRENT_POWER = "CurrentPower"
	DN = "Dn"
	DYN_REALLOC = "DynRealloc"
	GROUP_NAME = "GroupName"
	IDLE_POWER = "IdlePower"
	MAX_POWER = "MaxPower"
	MIN_POWER = "MinPower"
	OPER_COMMITTED = "OperCommitted"
	OPER_MIN = "OperMin"
	OPER_PEAK = "OperPeak"
	OPER_STATE = "OperState"
	PRIO = "Prio"
	PSU_CAPACITY = "PsuCapacity"
	PSU_STATE = "PsuState"
	RN = "Rn"
	SCALED_WT = "ScaledWt"
	STATUS = "Status"
	STYLE = "Style"
	UPDATE_TIME = "UpdateTime"
	WEIGHT = "Weight"

	CONST_ADMIN_COMMITTED_UNBOUNDED = "unbounded"
	CONST_ADMIN_PEAK_UNBOUNDED = "unbounded"
	CONST_CAP_ACTION_CLOCK_DOWN = "clock-down"
	CONST_CAP_ACTION_NOTHING = "nothing"
	CONST_CAP_ACTION_THROTTLED = "throttled"
	CONST_CATALOG_POWER_UNBOUNDED = "unbounded"
	CONST_CURRENT_POWER_UNBOUNDED = "unbounded"
	CONST_DYN_REALLOC_CHASSIS = "chassis"
	CONST_DYN_REALLOC_NONE = "none"
	CONST_IDLE_POWER_UNBOUNDED = "unbounded"
	CONST_MAX_POWER_UNBOUNDED = "unbounded"
	CONST_MIN_POWER_UNBOUNDED = "unbounded"
	CONST_OPER_COMMITTED_UNBOUNDED = "unbounded"
	CONST_OPER_MIN_UNBOUNDED = "unbounded"
	CONST_OPER_PEAK_UNBOUNDED = "unbounded"
	CONST_OPER_STATE_BUDGETED = "budgeted"
	CONST_OPER_STATE_BUDGETING = "budgeting"
	CONST_OPER_STATE_DEPLOYED = "deployed"
	CONST_OPER_STATE_DEPLOYING = "deploying"
	CONST_OPER_STATE_DISCOVERY_RETRY = "discovery-retry"
	CONST_OPER_STATE_FIRMWARE_MISMATCH = "firmware-mismatch"
	CONST_OPER_STATE_NON_COMPLIANT = "non-compliant"
	CONST_OPER_STATE_NOT_CAPPED = "not-capped"
	CONST_PRIO_NO_CAP = "no-cap"
	CONST_PRIO_UTILITY = "utility"
	CONST_PSU_STATE_INSUFFICIENT = "insufficient"
	CONST_PSU_STATE_OK = "ok"
	CONST_STYLE_INTELLIGENT_POLICY_DRIVEN = "intelligent-policy-driven"
	CONST_STYLE_MANUAL_PER_BLADE = "manual-per-blade"
