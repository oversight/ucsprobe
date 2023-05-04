import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FirmwareUcscInfo(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FirmwareUcscInfo")

	@staticmethod
	def ClassId():
		return "firmwareUcscInfo"

	CONN_PROTOCOL = "ConnProtocol"
	DN = "Dn"
	HOST = "Host"
	RN = "Rn"
	STATUS = "Status"

	CONST_CONN_PROTOCOL_IPV4 = "ipv4"
	CONST_CONN_PROTOCOL_IPV6 = "ipv6"
	CONST_CONN_PROTOCOL_UNKNOWN = "unknown"
