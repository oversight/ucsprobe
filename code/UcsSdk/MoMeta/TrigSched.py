import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TrigSched(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"TrigSched")

	@staticmethod
	def ClassId():
		return "trigSched"

	ADMIN_STATE = "AdminState"
	DESCR = "Descr"
	DN = "Dn"
	FLG_INITIAL_ACTIVE = "FlgInitialActive"
	NAME = "Name"
	OPER_STATE = "OperState"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_ADMIN_STATE_TRIGGER = "trigger"
	CONST_ADMIN_STATE_TRIGGER_IMMEDIATE = "trigger-immediate"
	CONST_ADMIN_STATE_TRIGGERED = "triggered"
	CONST_ADMIN_STATE_UNTRIGGERED = "untriggered"
	CONST_ADMIN_STATE_USER_ACK = "user-ack"
	CONST_ADMIN_STATE_USER_DISCARD = "user-discard"
	CONST_FLG_INITIAL_ACTIVE_FALSE = "false"
	CONST_FLG_INITIAL_ACTIVE_NO = "no"
	CONST_FLG_INITIAL_ACTIVE_TRUE = "true"
	CONST_FLG_INITIAL_ACTIVE_YES = "yes"
	CONST_INT_ID_NONE = "none"
	CONST_OPER_STATE_CAP_REACHED = "cap-reached"
	CONST_OPER_STATE_FAILED = "failed"
	CONST_OPER_STATE_IN_PROGRESS = "in-progress"
	CONST_OPER_STATE_PENDING = "pending"
	CONST_OPER_STATE_TRIGGERED = "triggered"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
