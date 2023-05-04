import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricNetflowMonSrcRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricNetflowMonSrcRef")

	@staticmethod
	def ClassId():
		return "fabricNetflowMonSrcRef"

	DN = "Dn"
	ID = "Id"
	PROTOCOL = "Protocol"
	RN = "Rn"
	SOURCE_DN = "SourceDn"
	SOURCE_TYPE = "SourceType"
	STATUS = "Status"
	TYPE = "Type"

	CONST_PROTOCOL_NETFLOW = "netflow"
	CONST_SOURCE_TYPE_PORT_PROFILE = "port-profile"
	CONST_SOURCE_TYPE_VNIC = "vnic"
