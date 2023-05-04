import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FcpoolInitiators(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FcpoolInitiators")

	@staticmethod
	def ClassId():
		return "fcpoolInitiators"

	ASSIGNED = "Assigned"
	ASSIGNMENT_ORDER = "AssignmentOrder"
	DESCR = "Descr"
	DN = "Dn"
	MAX_PORTS_PER_NODE = "MaxPortsPerNode"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PURPOSE = "Purpose"
	RN = "Rn"
	SIZE = "Size"
	STATUS = "Status"

	CONST_ASSIGNMENT_ORDER_DEFAULT = "default"
	CONST_ASSIGNMENT_ORDER_SEQUENTIAL = "sequential"
	CONST_INT_ID_NONE = "none"
	CONST_MAX_PORTS_PER_NODE_UPTO15 = "upto15"
	CONST_MAX_PORTS_PER_NODE_UPTO3 = "upto3"
	CONST_MAX_PORTS_PER_NODE_UPTO31 = "upto31"
	CONST_MAX_PORTS_PER_NODE_UPTO63 = "upto63"
	CONST_MAX_PORTS_PER_NODE_UPTO7 = "upto7"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_PURPOSE_NODE_AND_PORT_WWN_ASSIGNMENT = "node-and-port-wwn-assignment"
	CONST_PURPOSE_NODE_WWN_ASSIGNMENT = "node-wwn-assignment"
	CONST_PURPOSE_PORT_WWN_ASSIGNMENT = "port-wwn-assignment"
