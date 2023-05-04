import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PowerPrioWght(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PowerPrioWght")

	@staticmethod
	def ClassId():
		return "powerPrioWght"

	DN = "Dn"
	PRIO = "Prio"
	RN = "Rn"
	STATUS = "Status"
	WEIGHT = "Weight"

	CONST_PRIO_NO_CAP = "no-cap"
	CONST_PRIO_UTILITY = "utility"
