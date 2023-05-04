import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricVsanMembership(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricVsanMembership")

	@staticmethod
	def ClassId():
		return "fabricVsanMembership"

	DN = "Dn"
	MEMBER_STATUS = "MemberStatus"
	PARENT_ADMIN_STATE = "ParentAdminState"
	RN = "Rn"
	STATE_QUAL = "StateQual"
	STATUS = "Status"
	VSAN_ID = "VsanId"

	CONST_MEMBER_STATUS_DOWN = "down"
	CONST_MEMBER_STATUS_UP = "up"
	CONST_PARENT_ADMIN_STATE_DISABLED = "disabled"
	CONST_PARENT_ADMIN_STATE_ENABLED = "enabled"
