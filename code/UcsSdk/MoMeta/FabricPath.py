import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricPath(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricPath")

	@staticmethod
	def ClassId():
		return "fabricPath"

	C_TYPE = "CType"
	CHASSIS_ID = "ChassisId"
	DN = "Dn"
	ENACP = "Enacp"
	ID = "Id"
	LOCALE = "Locale"
	NAME = "Name"
	NS_SIZE = "NsSize"
	RN = "Rn"
	SIDE = "Side"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_C_TYPE_MUX = "mux"
	CONST_C_TYPE_MUX_ACCESS = "mux-access"
	CONST_C_TYPE_MUX_FABRIC = "mux-fabric"
	CONST_C_TYPE_MUX_FABRICPC = "mux-fabricpc"
	CONST_C_TYPE_MUX_FABRICPC_TO_HOSTPC = "mux-fabricpc-to-hostpc"
	CONST_C_TYPE_MUX_FABRICPC_TO_HOSTPORT = "mux-fabricpc-to-hostport"
	CONST_C_TYPE_MUX_FABRICPORT_TO_HOSTPC = "mux-fabricport-to-hostpc"
	CONST_C_TYPE_MUX_HOSTPC_TO_ADAPTORPC = "mux-hostpc-to-adaptorpc"
	CONST_C_TYPE_MUX_TO_CHASSIS = "mux-to-chassis"
	CONST_C_TYPE_MUX_TO_HOST = "mux-to-host"
	CONST_C_TYPE_SWITCH_ACCESS = "switch-access"
	CONST_C_TYPE_SWITCH_FABRIC = "switch-fabric"
	CONST_C_TYPE_SWITCH_FABRICPC = "switch-fabricpc"
	CONST_C_TYPE_SWITCH_TO_HOST = "switch-to-host"
	CONST_C_TYPE_SWITCH_TO_MUX = "switch-to-mux"
	CONST_CHASSIS_ID_N_A = "N/A"
	CONST_ENACP_CONSOLIDATED = "consolidated"
	CONST_ENACP_VIRTUAL = "virtual"
	CONST_SIDE_LEFT = "left"
	CONST_SIDE_RIGHT = "right"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
