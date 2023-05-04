import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeManager(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeManager")

	@staticmethod
	def ClassId():
		return "apeManager"

	DN = "Dn"
	RN = "Rn"
	STATS_UPDATE_ID = "StatsUpdateId"
	STATUS = "Status"

