import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IppoolPoolable(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IppoolPoolable")

	@staticmethod
	def ClassId():
		return "ippoolPoolable"

	DN = "Dn"
	ID = "Id"
	POOL_DN = "PoolDn"
	RN = "Rn"
	STATUS = "Status"

