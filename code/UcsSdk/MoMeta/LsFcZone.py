import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsFcZone(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsFcZone")

	@staticmethod
	def ClassId():
		return "lsFcZone"

	ADMIN_STATE = "AdminState"
	DN = "Dn"
	ID = "Id"
	IDENTITY = "Identity"
	INI_NAME = "IniName"
	NAME = "Name"
	OPER_STATE = "OperState"
	PEER_DN = "PeerDn"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	USR_LBL = "UsrLbl"
	VNET_ID = "VnetId"
	ZONING_TYPE = "ZoningType"

	CONST_ADMIN_STATE_ACTIVE = "active"
	CONST_ADMIN_STATE_APPLIED = "applied"
	CONST_ADMIN_STATE_APPLY_PENDING = "apply-pending"
	CONST_ADMIN_STATE_APPLYING = "applying"
	CONST_ADMIN_STATE_CREATE_FAILED = "create-failed"
	CONST_ADMIN_STATE_CREATED = "created"
	CONST_ADMIN_STATE_DELETED = "deleted"
	CONST_ADMIN_STATE_NOT_ACTIVE = "not-active"
	CONST_ADMIN_STATE_NOT_APPLIED = "not-applied"
	CONST_ADMIN_STATE_ZONE_MERGE_FAILURE = "zone-merge-failure"
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
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_ZONING_TYPE_NONE = "none"
	CONST_ZONING_TYPE_SIMT = "simt"
	CONST_ZONING_TYPE_SIST = "sist"
