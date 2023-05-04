import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricNetGroup(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricNetGroup")

	@staticmethod
	def ClassId():
		return "fabricNetGroup"

	ASSIGNED = "Assigned"
	ASSIGNMENT_ORDER = "AssignmentOrder"
	DESCR = "Descr"
	DN = "Dn"
	ID = "Id"
	NAME = "Name"
	NATIVE_NET = "NativeNet"
	NATIVE_NET_DN = "NativeNetDn"
	OWNER = "Owner"
	PEER_DN = "PeerDn"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	SIZE = "Size"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TYPE = "Type"

	CONST_ASSIGNMENT_ORDER_DEFAULT = "default"
	CONST_ASSIGNMENT_ORDER_SEQUENTIAL = "sequential"
	CONST_INT_ID_NONE = "none"
	CONST_OWNER_MANAGEMENT = "management"
	CONST_OWNER_POLICY = "policy"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_SWITCH_ID_DUAL = "dual"
