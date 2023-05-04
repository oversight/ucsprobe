import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtBackupPolicyConfig(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtBackupPolicyConfig")

	@staticmethod
	def ClassId():
		return "mgmtBackupPolicyConfig"

	ADMIN_STATE = "AdminState"
	AUTO_DELETE = "AutoDelete"
	BACKUP_DATE = "BackupDate"
	BACKUP_ISSUE = "BackupIssue"
	DESCR = "Descr"
	DN = "Dn"
	IGNORE_CAP = "IgnoreCap"
	NAME = "Name"
	OPER_SCHEDULER = "OperScheduler"
	OPER_STATE = "OperState"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SCHEDULER = "Scheduler"
	STATUS = "Status"

	CONST_ADMIN_STATE_TRIGGER = "trigger"
	CONST_ADMIN_STATE_TRIGGER_IMMEDIATE = "trigger-immediate"
	CONST_ADMIN_STATE_TRIGGERED = "triggered"
	CONST_ADMIN_STATE_UNTRIGGERED = "untriggered"
	CONST_ADMIN_STATE_USER_ACK = "user-ack"
	CONST_ADMIN_STATE_USER_DISCARD = "user-discard"
	CONST_AUTO_DELETE_FALSE = "false"
	CONST_AUTO_DELETE_NO = "no"
	CONST_AUTO_DELETE_TRUE = "true"
	CONST_AUTO_DELETE_YES = "yes"
	CONST_BACKUP_ISSUE_NONE = "none"
	CONST_BACKUP_ISSUE_OUTDATED = "outdated"
	CONST_IGNORE_CAP_FALSE = "false"
	CONST_IGNORE_CAP_NO = "no"
	CONST_IGNORE_CAP_TRUE = "true"
	CONST_IGNORE_CAP_YES = "yes"
	CONST_INT_ID_NONE = "none"
	CONST_OPER_STATE_ACTIVE = "active"
	CONST_OPER_STATE_APPLIED = "applied"
	CONST_OPER_STATE_APPLY_PENDING = "apply-pending"
	CONST_OPER_STATE_EVALUATED = "evaluated"
	CONST_OPER_STATE_EVALUATION_PENDING = "evaluation-pending"
	CONST_OPER_STATE_EXPIRED = "expired"
	CONST_OPER_STATE_NONE = "none"
	CONST_OPER_STATE_PENDING = "pending"
	CONST_OPER_STATE_UNTRIGGERED = "untriggered"
	CONST_OPER_STATE_WAITING_FOR_DEPENDENCY = "waiting-for-dependency"
	CONST_OPER_STATE_WAITING_FOR_MAINT_WINDOW = "waiting-for-maint-window"
	CONST_OPER_STATE_WAITING_FOR_USER = "waiting-for-user"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
