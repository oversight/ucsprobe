import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePhysicalAssocCtx(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePhysicalAssocCtx")

	@staticmethod
	def ClassId():
		return "computePhysicalAssocCtx"

	DN = "Dn"
	FRU_CAP_DN = "FruCapDn"
	RN = "Rn"
	STATUS = "Status"

