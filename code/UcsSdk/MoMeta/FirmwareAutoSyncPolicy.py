import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareAutoSyncPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareAutoSyncPolicy")

	@staticmethod
	def ClassId():
		return "firmwareAutoSyncPolicy"

	CONFIG_ISSUE = "ConfigIssue"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	SYNC_STATE = "SyncState"

	CONST_CONFIG_ISSUE_DEFAULT_PACKAGE_MISSING = "Default Package Missing"
	CONST_CONFIG_ISSUE_NO_ISSUES = "No Issues"
	CONST_CONFIG_ISSUE_VERSIONS_EMPTY_IN_DEFAULT_PACKAGE = "Versions Empty in Default Package"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SYNC_STATE_AUTO_ACKNOWLEDGE = "Auto Acknowledge"
	CONST_SYNC_STATE_NO_ACTIONS = "No Actions"
	CONST_SYNC_STATE_USER_ACKNOWLEDGE = "User Acknowledge"
