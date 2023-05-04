import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPortGroupDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPortGroupDef")

	@staticmethod
	def ClassId():
		return "equipmentPortGroupDef"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	NUMBER_OF_PORTS = "NumberOfPorts"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	TYPE = "Type"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_TYPE_ADAPTOR_EXT = "adaptor-ext"
	CONST_TYPE_ADAPTOR_PC = "adaptor-pc"
	CONST_TYPE_FABRIC = "fabric"
	CONST_TYPE_FABRIC_PC = "fabric-pc"
	CONST_TYPE_HOST = "host"
	CONST_TYPE_HOST_PC = "host-pc"
	CONST_TYPE_SERVER_PC = "server-pc"
	CONST_TYPE_SWITCH_ETHER = "switch-ether"
	CONST_TYPE_SWITCH_FC = "switch-fc"
