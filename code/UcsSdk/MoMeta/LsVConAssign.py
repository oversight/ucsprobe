import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LsVConAssign(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"LsVConAssign")

	@staticmethod
	def ClassId():
		return "lsVConAssign"

	ADMIN_VCON = "AdminVcon"
	DN = "Dn"
	ORDER = "Order"
	RN = "Rn"
	STATUS = "Status"
	TRANSPORT = "Transport"
	VNIC_NAME = "VnicName"

	CONST_ADMIN_VCON_1 = "1"
	CONST_ADMIN_VCON_2 = "2"
	CONST_ADMIN_VCON_3 = "3"
	CONST_ADMIN_VCON_4 = "4"
	CONST_ADMIN_VCON_ANY = "any"
	CONST_ORDER_UNSPECIFIED = "unspecified"
