import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIScsiBootVnic(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIScsiBootVnic")

	@staticmethod
	def ClassId():
		return "vnicIScsiBootVnic"

	AUTH_PROFILE_NAME = "AuthProfileName"
	DESCR = "Descr"
	DN = "Dn"
	INITIATOR_NAME = "InitiatorName"
	IQN_IDENT_POOL_NAME = "IqnIdentPoolName"
	NAME = "Name"
	OPER_AUTH_PROFILE_NAME = "OperAuthProfileName"
	OPER_IQN_IDENT_POOL_NAME = "OperIqnIdentPoolName"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
