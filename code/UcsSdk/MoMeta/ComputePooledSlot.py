import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePooledSlot(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePooledSlot")

	@staticmethod
	def ClassId():
		return "computePooledSlot"

	ASSIGNED = "Assigned"
	ASSIGNED_TO_DN = "AssignedToDn"
	CHASSIS_ID = "ChassisId"
	DN = "Dn"
	OWNER = "Owner"
	POOLABLE_DN = "PoolableDn"
	PREV_ASSIGNED_TO_DN = "PrevAssignedToDn"
	RN = "Rn"
	SLOT_ID = "SlotId"
	STATUS = "Status"

	CONST_ASSIGNED_FALSE = "false"
	CONST_ASSIGNED_NO = "no"
	CONST_ASSIGNED_TRUE = "true"
	CONST_ASSIGNED_YES = "yes"
	CONST_CHASSIS_ID_N_A = "N/A"
	CONST_OWNER_MANAGEMENT = "management"
	CONST_OWNER_POLICY = "policy"
