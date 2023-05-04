import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIPv4PooledIscsiAddr(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIPv4PooledIscsiAddr")

	@staticmethod
	def ClassId():
		return "vnicIPv4PooledIscsiAddr"

	ADDR = "Addr"
	DEF_GW = "DefGw"
	DN = "Dn"
	IDENT_POOL_NAME = "IdentPoolName"
	OPER_IDENT_POOL_NAME = "OperIdentPoolName"
	PRIM_DNS = "PrimDns"
	RN = "Rn"
	SEC_DNS = "SecDns"
	STATUS = "Status"
	SUBNET = "Subnet"

