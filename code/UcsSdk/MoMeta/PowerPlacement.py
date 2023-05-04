import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PowerPlacement(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PowerPlacement")

	@staticmethod
	def ClassId():
		return "powerPlacement"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	PEER_REQ_CONFLICT = "PeerReqConflict"
	PG_NAME = "PgName"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PRIO_SHARE = "PrioShare"
	RN = "Rn"
	SELF_REQ_CONFLICT = "SelfReqConflict"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_PEER_REQ_CONFLICT_FAIL_PLACEMENT = "fail-placement"
	CONST_PEER_REQ_CONFLICT_IGNORE = "ignore"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PRIO_SHARE_HIGHEST_PRIO_IN_CHASSIS = "highest-prio-in-chassis"
	CONST_PRIO_SHARE_HIGHEST_PRIO_IN_POWER_GROUP = "highest-prio-in-power-group"
	CONST_PRIO_SHARE_NO_PREFERENCE = "no-preference"
	CONST_SELF_REQ_CONFLICT_FAIL_PLACEMENT = "fail-placement"
	CONST_SELF_REQ_CONFLICT_IGNORE = "ignore"
