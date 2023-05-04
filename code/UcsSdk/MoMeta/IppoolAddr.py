import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IppoolAddr(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IppoolAddr")

	@staticmethod
	def ClassId():
		return "ippoolAddr"

	ASSIGNED = "Assigned"
	ASSIGNED_TO_DN = "AssignedToDn"
	DN = "Dn"
	ID = "Id"
	OWNER = "Owner"
	RN = "Rn"
	STATUS = "Status"

	CONST_ASSIGNED_FALSE = "false"
	CONST_ASSIGNED_NO = "no"
	CONST_ASSIGNED_TRUE = "true"
	CONST_ASSIGNED_YES = "yes"
	CONST_OWNER_END_POINT = "end-point"
	CONST_OWNER_POOL = "pool"
