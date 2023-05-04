import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtAccessPort(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtAccessPort")

	@staticmethod
	def ClassId():
		return "mgmtAccessPort"

	DN = "Dn"
	PORT = "Port"
	PROTOCOL = "Protocol"
	RN = "Rn"
	STATUS = "Status"

	CONST_PORT_NONE = "none"
	CONST_PROTOCOL_TCP = "TCP"
	CONST_PROTOCOL_UDP = "UDP"
