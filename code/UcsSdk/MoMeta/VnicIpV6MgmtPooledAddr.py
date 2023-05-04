import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicIpV6MgmtPooledAddr(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicIpV6MgmtPooledAddr")

	@staticmethod
	def ClassId():
		return "vnicIpV6MgmtPooledAddr"

	ADDR = "Addr"
	DEF_GW = "DefGw"
	DN = "Dn"
	NAME = "Name"
	OPER_NAME = "OperName"
	PREFIX = "Prefix"
	PRIM_DNS = "PrimDns"
	RN = "Rn"
	SEC_DNS = "SecDns"
	STATUS = "Status"

