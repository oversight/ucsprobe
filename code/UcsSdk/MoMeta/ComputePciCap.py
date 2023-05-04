import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ComputePciCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ComputePciCap")

	@staticmethod
	def ClassId():
		return "computePciCap"

	DN = "Dn"
	MAX_BUS_ID_PER_SLOT = "MaxBusIdPerSlot"
	NUM_OF_PHYS_SLOTS = "NumOfPhysSlots"
	ORDER = "Order"
	RN = "Rn"
	STARTS_WITH = "StartsWith"
	STATUS = "Status"

	CONST_ORDER_ASCENDING = "ascending"
	CONST_ORDER_ASCENDING_DUAL = "ascending-dual"
	CONST_ORDER_ASCENDING_EXTENDED = "ascending-extended"
	CONST_ORDER_ASCENDING_SEQ = "ascending-seq"
	CONST_ORDER_DESCENDING = "descending"
