import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ObserveObservedCont(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ObserveObservedCont")

	@staticmethod
	def ClassId():
		return "observeObservedCont"

	DN = "Dn"
	ID_COUNT = "IdCount"
	RN = "Rn"
	STATUS = "Status"

