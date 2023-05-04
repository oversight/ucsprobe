import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputeRackQual(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputeRackQual")

	@staticmethod
	def ClassId():
		return "computeRackQual"

	DN = "Dn"
	MAX_ID = "MaxId"
	MIN_ID = "MinId"
	RN = "Rn"
	STATUS = "Status"

