import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicLanConnTempl(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicLanConnTempl")

	@staticmethod
	def ClassId():
		return "vnicLanConnTempl"

	DESCR = "Descr"
	DN = "Dn"
	IDENT_POOL_NAME = "IdentPoolName"
	MTU = "Mtu"
	NAME = "Name"
	NW_CTRL_POLICY_NAME = "NwCtrlPolicyName"
	OPER_IDENT_POOL_NAME = "OperIdentPoolName"
	OPER_NW_CTRL_POLICY_NAME = "OperNwCtrlPolicyName"
	OPER_QOS_POLICY_NAME = "OperQosPolicyName"
	OPER_STATS_POLICY_NAME = "OperStatsPolicyName"
	PIN_TO_GROUP_NAME = "PinToGroupName"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	QOS_POLICY_NAME = "QosPolicyName"
	RN = "Rn"
	STATS_POLICY_NAME = "StatsPolicyName"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TARGET = "Target"
	TEMPL_TYPE = "TemplType"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_A_B = "A-B"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_B_A = "B-A"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_TEMPL_TYPE_INITIAL_TEMPLATE = "initial-template"
	CONST_TEMPL_TYPE_UPDATING_TEMPLATE = "updating-template"
