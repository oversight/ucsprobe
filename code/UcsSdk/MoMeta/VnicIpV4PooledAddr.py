import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIpV4PooledAddr(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIpV4PooledAddr")

	@staticmethod
	def ClassId():
		return "vnicIpV4PooledAddr"

	ADDR = "Addr"
	DEF_GW = "DefGw"
	DN = "Dn"
	NAME = "Name"
	OPER_NAME = "OperName"
	PRIM_DNS = "PrimDns"
	RN = "Rn"
	SEC_DNS = "SecDns"
	STATUS = "Status"
	SUBNET = "Subnet"

