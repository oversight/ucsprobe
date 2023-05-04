import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtBackupExportExtPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtBackupExportExtPolicy")

	@staticmethod
	def ClassId():
		return "mgmtBackupExportExtPolicy"

	ADMIN_STATE = "AdminState"
	DESCR = "Descr"
	DN = "Dn"
	FREQUENCY = "Frequency"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_ADMIN_STATE_DISABLE = "disable"
	CONST_ADMIN_STATE_ENABLE = "enable"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
