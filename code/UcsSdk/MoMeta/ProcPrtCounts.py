import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProcPrtCounts(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ProcPrtCounts")

	@staticmethod
	def ClassId():
		return "procPrtCounts"

	CACHENOSPC = "Cachenospc"
	DBTXS = "Dbtxs"
	DN = "Dn"
	LARGETXS = "Largetxs"
	PERSIST_TIME = "PersistTime"
	RN = "Rn"
	STATUS = "Status"
	TOTAL = "Total"

