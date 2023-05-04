import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIPv4IscsiAddr(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIPv4IscsiAddr")

	@staticmethod
	def ClassId():
		return "vnicIPv4IscsiAddr"

	ADDR = "Addr"
	DEF_GW = "DefGw"
	DN = "Dn"
	PRIM_DNS = "PrimDns"
	RN = "Rn"
	SEC_DNS = "SecDns"
	STATUS = "Status"
	SUBNET = "Subnet"

