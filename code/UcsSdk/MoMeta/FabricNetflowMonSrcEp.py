import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricNetflowMonSrcEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricNetflowMonSrcEp")

	@staticmethod
	def ClassId():
		return "fabricNetflowMonSrcEp"

	DN = "Dn"
	NAME = "Name"
	PROTOCOL = "Protocol"
	RN = "Rn"
	SESSION = "Session"
	STATUS = "Status"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_PROTOCOL_NETFLOW = "netflow"
