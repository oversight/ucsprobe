import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IppoolIpV6Block(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IppoolIpV6Block")

	@staticmethod
	def ClassId():
		return "ippoolIpV6Block"

	DEF_GW = "DefGw"
	DN = "Dn"
	FROM = "From"
	PREFIX = "Prefix"
	PRIM_DNS = "PrimDns"
	RN = "Rn"
	SEC_DNS = "SecDns"
	STATUS = "Status"
	TO = "To"

