import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwatResultstats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwatResultstats")

	@staticmethod
	def ClassId():
		return "swatResultstats"

	ACTIVITY_NAME = "ActivityName"
	DN = "Dn"
	FALSE_HITS = "FalseHits"
	LABEL = "Label"
	RN = "Rn"
	STATUS = "Status"
	TOTAL_PASSES = "TotalPasses"
	TRUE_HITS = "TrueHits"

