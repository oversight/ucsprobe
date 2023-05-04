import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwFcZone(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwFcZone")

	@staticmethod
	def ClassId():
		return "swFcZone"

	DN = "Dn"
	ID = "Id"
	IDENTITY = "Identity"
	LC = "Lc"
	NAME = "Name"
	OPER_STATE = "OperState"
	PEER_DN = "PeerDn"
	RN = "Rn"
	STATUS = "Status"

	CONST_LC_ALLOCATED = "allocated"
	CONST_LC_AVAILABLE = "available"
	CONST_LC_DEALLOCATED = "deallocated"
	CONST_LC_REPURPOSED = "repurposed"
	CONST_OPER_STATE_ACTIVE = "active"
	CONST_OPER_STATE_APPLIED = "applied"
	CONST_OPER_STATE_APPLY_PENDING = "apply-pending"
	CONST_OPER_STATE_APPLYING = "applying"
	CONST_OPER_STATE_CREATE_FAILED = "create-failed"
	CONST_OPER_STATE_CREATED = "created"
	CONST_OPER_STATE_DELETED = "deleted"
	CONST_OPER_STATE_NOT_ACTIVE = "not-active"
	CONST_OPER_STATE_NOT_APPLIED = "not-applied"
	CONST_OPER_STATE_ZONE_MERGE_FAILURE = "zone-merge-failure"
