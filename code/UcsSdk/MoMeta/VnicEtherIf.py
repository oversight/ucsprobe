import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicEtherIf(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicEtherIf")

	@staticmethod
	def ClassId():
		return "vnicEtherIf"

	ADDR = "Addr"
	CONFIG_QUALIFIER = "ConfigQualifier"
	DEFAULT_NET = "DefaultNet"
	DN = "Dn"
	NAME = "Name"
	OPER_STATE = "OperState"
	OPER_VNET_DN = "OperVnetDn"
	OPER_VNET_NAME = "OperVnetName"
	OWNER = "Owner"
	PUB_NW_ID = "PubNwId"
	RN = "Rn"
	SHARING = "Sharing"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TYPE = "Type"
	VNET = "Vnet"

	CONST_ADDR_DERIVED = "derived"
	CONST_DEFAULT_NET_FALSE = "false"
	CONST_DEFAULT_NET_NO = "no"
	CONST_DEFAULT_NET_TRUE = "true"
	CONST_DEFAULT_NET_YES = "yes"
	CONST_OPER_STATE_DOWN = "down"
	CONST_OPER_STATE_FAILED = "failed"
	CONST_OPER_STATE_INDETERMINATE = "indeterminate"
	CONST_OPER_STATE_UP = "up"
	CONST_OWNER_CONN_POLICY = "conn_policy"
	CONST_OWNER_LOGICAL = "logical"
	CONST_OWNER_PHYSICAL = "physical"
	CONST_OWNER_POLICY = "policy"
	CONST_OWNER_UNKNOWN = "unknown"
	CONST_SHARING_COMMUNITY = "community"
	CONST_SHARING_ISOLATED = "isolated"
	CONST_SHARING_NONE = "none"
	CONST_SHARING_PRIMARY = "primary"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_A_B = "A-B"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_B_A = "B-A"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_TYPE_ETHER = "ether"
	CONST_TYPE_FC = "fc"
	CONST_TYPE_IPC = "ipc"
	CONST_TYPE_SCSI = "scsi"
	CONST_TYPE_UNKNOWN = "unknown"
