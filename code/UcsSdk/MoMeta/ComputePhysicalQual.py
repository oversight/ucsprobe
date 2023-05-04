import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePhysicalQual(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePhysicalQual")

	@staticmethod
	def ClassId():
		return "computePhysicalQual"

	DN = "Dn"
	MODEL = "Model"
	RN = "Rn"
	STATUS = "Status"

