import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FcpoolInitiator(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FcpoolInitiator")

	@staticmethod
	def ClassId():
		return "fcpoolInitiator"

	ASSIGNED = "Assigned"
	ASSIGNED_TO_DN = "AssignedToDn"
	DESCR = "Descr"
	DN = "Dn"
	ID = "Id"
	NAME = "Name"
	POOLABLE_DN = "PoolableDn"
	PREV_ASSIGNED_TO_DN = "PrevAssignedToDn"
	PURPOSE = "Purpose"
	RN = "Rn"
	STATUS = "Status"

	CONST_ASSIGNED_FALSE = "false"
	CONST_ASSIGNED_NO = "no"
	CONST_ASSIGNED_TRUE = "true"
	CONST_ASSIGNED_YES = "yes"
	CONST_PURPOSE_DERIVED = "derived"
	CONST_PURPOSE_NODE_WWN = "node-wwn"
	CONST_PURPOSE_PORT_WWN = "port-wwn"
