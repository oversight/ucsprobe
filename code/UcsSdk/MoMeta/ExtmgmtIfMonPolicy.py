import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ExtmgmtIfMonPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ExtmgmtIfMonPolicy")

	@staticmethod
	def ClassId():
		return "extmgmtIfMonPolicy"

	ADMIN_STATE = "AdminState"
	DESCR = "Descr"
	DN = "Dn"
	ENABLE_HAFAILOVER = "EnableHAFailover"
	MAX_FAIL_REPORT_COUNT = "MaxFailReportCount"
	MONITOR_MECHANISM = "MonitorMechanism"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	POLL_INTERVAL = "PollInterval"
	RN = "Rn"
	STATUS = "Status"

	CONST_ADMIN_STATE_DISABLED = "disabled"
	CONST_ADMIN_STATE_ENABLED = "enabled"
	CONST_ENABLE_HAFAILOVER_FALSE = "false"
	CONST_ENABLE_HAFAILOVER_NO = "no"
	CONST_ENABLE_HAFAILOVER_TRUE = "true"
	CONST_ENABLE_HAFAILOVER_YES = "yes"
	CONST_INT_ID_NONE = "none"
	CONST_MONITOR_MECHANISM_ARP_TARGET_PING = "arpTargetPing"
	CONST_MONITOR_MECHANISM_GATEWAY_PING = "gatewayPing"
	CONST_MONITOR_MECHANISM_MII_STATUS = "miiStatus"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
