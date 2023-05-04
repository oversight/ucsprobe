import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricNetflowCollector(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricNetflowCollector")

	@staticmethod
	def ClassId():
		return "fabricNetflowCollector"

	DESCR = "Descr"
	DN = "Dn"
	FLOW_PROTOCOL = "FlowProtocol"
	ID = "Id"
	LOCALE = "Locale"
	NAME = "Name"
	PORT = "Port"
	RN = "Rn"
	SOURCE_VLAN = "SourceVlan"
	SOURCE_VLAN_DN = "SourceVlanDn"
	STATUS = "Status"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_FLOW_PROTOCOL_NETFLOW = "netflow"
	CONST_ID_A = "A"
	CONST_ID_B = "B"
	CONST_ID_NONE = "NONE"
