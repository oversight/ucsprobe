import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeSlotQual(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeSlotQual")

	@staticmethod
	def ClassId():
		return "computeSlotQual"

	DN = "Dn"
	MAX_ID = "MaxId"
	MIN_ID = "MinId"
	RN = "Rn"
	STATUS = "Status"

