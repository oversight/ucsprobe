import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IdentIdentCtx(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IdentIdentCtx")

	@staticmethod
	def ClassId():
		return "identIdentCtx"

	ASSIGNED = "Assigned"
	CONS_DN = "ConsDn"
	CONS_TYPE = "ConsType"
	DEFINED_IN_IDM = "DefinedInIdm"
	DN = "Dn"
	IDENT_POOL_NAME = "IdentPoolName"
	IDENT_TYPE = "IdentType"
	INTENT = "Intent"
	POOL_DN = "PoolDn"
	POOL_ORG_DN = "PoolOrgDn"
	POOLED_ID = "PooledId"
	RET_STATUS = "RetStatus"
	RN = "Rn"
	SEQ_NUM = "SeqNum"
	STATUS = "Status"
	SUPPL_ID1 = "SupplId1"
	SUPPL_ID2 = "SupplId2"
	SUPPL_ID3 = "SupplId3"
	SUPPL_ID4 = "SupplId4"

	CONST_CONS_TYPE_CHASSIS = "chassis"
	CONST_CONS_TYPE_SERVER = "server"
	CONST_CONS_TYPE_VHBA = "vhba"
	CONST_CONS_TYPE_VM = "vm"
	CONST_CONS_TYPE_VMNIC = "vmnic"
	CONST_CONS_TYPE_VNIC = "vnic"
	CONST_DEFINED_IN_IDM_NO = "no"
	CONST_DEFINED_IN_IDM_YES = "yes"
	CONST_IDENT_TYPE_IP_V4 = "ipV4"
	CONST_IDENT_TYPE_IP_V6 = "ipV6"
	CONST_IDENT_TYPE_IQN = "iqn"
	CONST_IDENT_TYPE_MAC = "mac"
	CONST_IDENT_TYPE_UUID = "uuid"
	CONST_IDENT_TYPE_VLAN = "vlan"
	CONST_IDENT_TYPE_WWNN = "wwnn"
	CONST_IDENT_TYPE_WWPN = "wwpn"
	CONST_INTENT_ADD_POOLED = "add-pooled"
	CONST_INTENT_ASSIGN = "assign"
	CONST_INTENT_DELETE_POOLED = "delete-pooled"
	CONST_INTENT_REQUISITION = "requisition"
	CONST_INTENT_UNASSIGN = "unassign"
	CONST_RET_STATUS_ASSIGNED_BY_OTHER = "assigned-by-other"
	CONST_RET_STATUS_FAILED = "failed"
	CONST_RET_STATUS_OUT_OF_SYNC = "out-of-sync"
	CONST_RET_STATUS_SUCCEEDED = "succeeded"
	CONST_RET_STATUS_SYNCED = "synced"
