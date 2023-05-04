import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIScsiNode(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIScsiNode")

	@staticmethod
	def ClassId():
		return "vnicIScsiNode"

	DN = "Dn"
	INIT_NAME_SUFFIX = "InitNameSuffix"
	INITIATOR_NAME = "InitiatorName"
	IQN_IDENT_POOL_NAME = "IqnIdentPoolName"
	OPER_IQN_IDENT_POOL_NAME = "OperIqnIdentPoolName"
	OWNER = "Owner"
	RN = "Rn"
	STATUS = "Status"

	CONST_OWNER_CONN_POLICY = "conn_policy"
	CONST_OWNER_LOGICAL = "logical"
	CONST_OWNER_PHYSICAL = "physical"
	CONST_OWNER_POLICY = "policy"
	CONST_OWNER_UNKNOWN = "unknown"
