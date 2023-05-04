import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricUdldPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricUdldPolicy")

	@staticmethod
	def ClassId():
		return "fabricUdldPolicy"

	DESCR = "Descr"
	DN = "Dn"
	MSG_INTERVAL = "MsgInterval"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RECOVERY_ACTION = "RecoveryAction"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_RECOVERY_ACTION_NONE = "none"
	CONST_RECOVERY_ACTION_RESET = "reset"
