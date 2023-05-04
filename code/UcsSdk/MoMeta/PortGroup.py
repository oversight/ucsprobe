import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PortGroup(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PortGroup")

	@staticmethod
	def ClassId():
		return "portGroup"

	DN = "Dn"
	LOCALE = "Locale"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_TYPE_ADAPTOR_EXT = "adaptor-ext"
	CONST_TYPE_ADAPTOR_PC = "adaptor-pc"
	CONST_TYPE_FABRIC = "fabric"
	CONST_TYPE_FABRIC_PC = "fabric-pc"
	CONST_TYPE_HOST = "host"
	CONST_TYPE_HOST_PC = "host-pc"
	CONST_TYPE_SERVER_PC = "server-pc"
	CONST_TYPE_SWITCH_ETHER = "switch-ether"
	CONST_TYPE_SWITCH_FC = "switch-fc"
