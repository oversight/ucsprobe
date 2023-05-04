import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IppoolPooled(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IppoolPooled")

	@staticmethod
	def ClassId():
		return "ippoolPooled"

	ASSIGNED = "Assigned"
	ASSIGNED_TO_DN = "AssignedToDn"
	DEF_GW = "DefGw"
	DN = "Dn"
	ID = "Id"
	POOLABLE_DN = "PoolableDn"
	PREV_ASSIGNED_TO_DN = "PrevAssignedToDn"
	PRIM_DNS = "PrimDns"
	RN = "Rn"
	SEC_DNS = "SecDns"
	STATUS = "Status"
	SUBNET = "Subnet"

	CONST_ASSIGNED_FALSE = "false"
	CONST_ASSIGNED_NO = "no"
	CONST_ASSIGNED_TRUE = "true"
	CONST_ASSIGNED_YES = "yes"
