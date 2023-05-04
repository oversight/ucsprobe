import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricChangedObjectRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricChangedObjectRef")

	@staticmethod
	def ClassId():
		return "fabricChangedObjectRef"

	CENTRALE_VNET_EP_DN = "CentraleVnetEpDn"
	DN = "Dn"
	ID = "Id"
	OLD_CENTRALE_VNET_EP_DN = "OldCentraleVnetEpDn"
	REF_OBJ_STATUS = "RefObjStatus"
	RN = "Rn"
	STATUS = "Status"
	UCSM_VNET_EP_DN = "UcsmVnetEpDn"

	CONST_REF_OBJ_STATUS_CREATED = "created"
	CONST_REF_OBJ_STATUS_DELETED = "deleted"
	CONST_REF_OBJ_STATUS_INTENT_DELETION = "intent-deletion"
	CONST_REF_OBJ_STATUS_MODIFIED = "modified"
