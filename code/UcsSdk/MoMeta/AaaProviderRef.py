import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaProviderRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaProviderRef")

	@staticmethod
	def ClassId():
		return "aaaProviderRef"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	ORDER = "Order"
	RN = "Rn"
	STATUS = "Status"

	CONST_ORDER_LOWEST_AVAILABLE = "lowest-available"
