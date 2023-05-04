import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeChassisConnPolicy(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeChassisConnPolicy")

	@staticmethod
	def ClassId():
		return "computeChassisConnPolicy"

	ADMIN_STATE = "AdminState"
	CHASSIS_ID = "ChassisId"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	QUALIFIER = "Qualifier"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"

	CONST_ADMIN_STATE_GLOBAL = "global"
	CONST_ADMIN_STATE_NONE = "none"
	CONST_ADMIN_STATE_PORT_CHANNEL = "port-channel"
	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
