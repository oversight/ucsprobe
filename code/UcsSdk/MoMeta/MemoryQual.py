import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MemoryQual(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MemoryQual")

	@staticmethod
	def ClassId():
		return "memoryQual"

	CLOCK = "Clock"
	DN = "Dn"
	LATENCY = "Latency"
	MAX_CAP = "MaxCap"
	MIN_CAP = "MinCap"
	RN = "Rn"
	SPEED = "Speed"
	STATUS = "Status"
	UNITS = "Units"
	WIDTH = "Width"

	CONST_CLOCK_UNSPECIFIED = "unspecified"
	CONST_LATENCY_UNSPECIFIED = "unspecified"
	CONST_MAX_CAP_UNSPECIFIED = "unspecified"
	CONST_MIN_CAP_UNSPECIFIED = "unspecified"
	CONST_SPEED_UNSPECIFIED = "unspecified"
	CONST_UNITS_UNSPECIFIED = "unspecified"
	CONST_WIDTH_UNSPECIFIED = "unspecified"
