import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePsuControl(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePsuControl")

	@staticmethod
	def ClassId():
		return "computePsuControl"

	CLUSTER_STATE = "ClusterState"
	DESCR = "Descr"
	DN = "Dn"
	INPUT_POWER_STATE = "InputPowerState"
	NAME = "Name"
	OPER_QUALIFIER = "OperQualifier"
	OPER_STATE = "OperState"
	OUTPUT_POWER_STATE = "OutputPowerState"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	REDUNDANCY = "Redundancy"
	RN = "Rn"
	STATUS = "Status"

	CONST_CLUSTER_STATE_NOT_CLUSTERED = "not-clustered"
	CONST_CLUSTER_STATE_SLOT_1_MASTER = "slot-1-master"
	CONST_CLUSTER_STATE_SLOT_2_MASTER = "slot-2-master"
	CONST_CLUSTER_STATE_UNKNOWN = "unknown"
	CONST_INPUT_POWER_STATE_LOWER_CRITICAL = "lower-critical"
	CONST_INPUT_POWER_STATE_LOWER_NON_CRITICAL = "lower-non-critical"
	CONST_INPUT_POWER_STATE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
	CONST_INPUT_POWER_STATE_NOT_SUPPORTED = "not-supported"
	CONST_INPUT_POWER_STATE_OK = "ok"
	CONST_INPUT_POWER_STATE_UNKNOWN = "unknown"
	CONST_INPUT_POWER_STATE_UPPER_CRITICAL = "upper-critical"
	CONST_INPUT_POWER_STATE_UPPER_NON_CRITICAL = "upper-non-critical"
	CONST_INPUT_POWER_STATE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
	CONST_INT_ID_NONE = "none"
	CONST_OPER_STATE_DEGRADED = "degraded"
	CONST_OPER_STATE_FAILED = "failed"
	CONST_OPER_STATE_OK = "ok"
	CONST_OPER_STATE_UNKNOWN = "unknown"
	CONST_OUTPUT_POWER_STATE_LOWER_CRITICAL = "lower-critical"
	CONST_OUTPUT_POWER_STATE_LOWER_NON_CRITICAL = "lower-non-critical"
	CONST_OUTPUT_POWER_STATE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
	CONST_OUTPUT_POWER_STATE_NOT_SUPPORTED = "not-supported"
	CONST_OUTPUT_POWER_STATE_OK = "ok"
	CONST_OUTPUT_POWER_STATE_UNKNOWN = "unknown"
	CONST_OUTPUT_POWER_STATE_UPPER_CRITICAL = "upper-critical"
	CONST_OUTPUT_POWER_STATE_UPPER_NON_CRITICAL = "upper-non-critical"
	CONST_OUTPUT_POWER_STATE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_REDUNDANCY_GRID = "grid"
	CONST_REDUNDANCY_N_1 = "n+1"
	CONST_REDUNDANCY_NON_REDUNDANT = "non-redundant"
	CONST_REDUNDANCY_UNKNOWN = "unknown"
