import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IqnpoolPoolable(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"IqnpoolPoolable")

	@staticmethod
	def ClassId():
		return "iqnpoolPoolable"

	DN = "Dn"
	ID = "Id"
	POOL_DN = "PoolDn"
	RN = "Rn"
	STATUS = "Status"

