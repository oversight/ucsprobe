import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricPathConn(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricPathConn")

	@staticmethod
	def ClassId():
		return "fabricPathConn"

	C_TYPE = "CType"
	DN = "Dn"
	LOCALE = "Locale"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
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
