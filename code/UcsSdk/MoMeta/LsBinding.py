import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsBinding(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsBinding")

	@staticmethod
	def ClassId():
		return "lsBinding"

	ASSIGNED_TO_DN = "AssignedToDn"
	COMPUTE_EP_DN = "ComputeEpDn"
	DN = "Dn"
	ISSUES = "Issues"
	NAME = "Name"
	OPER_STATE = "OperState"
	PN_DN = "PnDn"
	RESTRICT_MIGRATION = "RestrictMigration"
	RN = "Rn"
	STATUS = "Status"

	CONST_OPER_STATE_FAILED_TO_APPLY = "failed-to-apply"
	CONST_OPER_STATE_UNUSED = "unused"
	CONST_OPER_STATE_USED = "used"
	CONST_RESTRICT_MIGRATION_FALSE = "false"
	CONST_RESTRICT_MIGRATION_NO = "no"
	CONST_RESTRICT_MIGRATION_TRUE = "true"
	CONST_RESTRICT_MIGRATION_YES = "yes"
