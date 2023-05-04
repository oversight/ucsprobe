import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IppoolBlock(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IppoolBlock")

	@staticmethod
	def ClassId():
		return "ippoolBlock"

	DEF_GW = "DefGw"
	DN = "Dn"
	FROM = "From"
	PRIM_DNS = "PrimDns"
	RN = "Rn"
	SEC_DNS = "SecDns"
	STATUS = "Status"
	SUBNET = "Subnet"
	TO = "To"

