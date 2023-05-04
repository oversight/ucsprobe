import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicFcNode(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicFcNode")

	@staticmethod
	def ClassId():
		return "vnicFcNode"

	ADDR = "Addr"
	DN = "Dn"
	IDENT_POOL_NAME = "IdentPoolName"
	MAX_DERIVABLE_WWPN = "MaxDerivableWWPN"
	OPER_IDENT_POOL_NAME = "OperIdentPoolName"
	OWNER = "Owner"
	RN = "Rn"
	STATUS = "Status"

	CONST_ADDR_POOL_DERIVED = "pool-derived"
	CONST_ADDR_VNIC_DERIVED = "vnic-derived"
	CONST_OWNER_CONN_POLICY = "conn_policy"
	CONST_OWNER_LOGICAL = "logical"
	CONST_OWNER_PHYSICAL = "physical"
	CONST_OWNER_POLICY = "policy"
	CONST_OWNER_UNKNOWN = "unknown"
