import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IqnpoolPooled(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IqnpoolPooled")

	@staticmethod
	def ClassId():
		return "iqnpoolPooled"

	ASSIGNED = "Assigned"
	ASSIGNED_TO_DN = "AssignedToDn"
	DN = "Dn"
	NAME = "Name"
	POOLABLE_DN = "PoolableDn"
	PREV_ASSIGNED_TO_DN = "PrevAssignedToDn"
	RN = "Rn"
	STATUS = "Status"

	CONST_ASSIGNED_FALSE = "false"
	CONST_ASSIGNED_NO = "no"
	CONST_ASSIGNED_TRUE = "true"
	CONST_ASSIGNED_YES = "yes"
