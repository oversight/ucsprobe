import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FaultPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FaultPolicy")

	@staticmethod
	def ClassId():
		return "faultPolicy"

	ACK_ACTION = "AckAction"
	CLEAR_ACTION = "ClearAction"
	CLEAR_INTERVAL = "ClearInterval"
	DESCR = "Descr"
	DN = "Dn"
	FLAP_INTERVAL = "FlapInterval"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RETENTION_INTERVAL = "RetentionInterval"
	RN = "Rn"
	SIZE_LIMIT = "SizeLimit"
	SOAK_INTERVAL = "SoakInterval"
	SOAKING_SEVERITY = "SoakingSeverity"
	STATUS = "Status"

	CONST_ACK_ACTION_DELETE_ON_CLEAR = "delete-on-clear"
	CONST_ACK_ACTION_INITIAL_SEVERITY = "initial-severity"
	CONST_CLEAR_ACTION_DELETE = "delete"
	CONST_CLEAR_ACTION_RETAIN = "retain"
	CONST_CLEAR_INTERVAL_NEVER = "never"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_RETENTION_INTERVAL_FOREVER = "forever"
	CONST_SIZE_LIMIT_MAX = "max"
	CONST_SOAK_INTERVAL_NEVER = "never"
	CONST_SOAKING_SEVERITY_CONDITION = "condition"
	CONST_SOAKING_SEVERITY_INFO = "info"
	CONST_SOAKING_SEVERITY_WARNING = "warning"
