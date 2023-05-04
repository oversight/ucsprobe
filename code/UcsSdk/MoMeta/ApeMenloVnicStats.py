import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeMenloVnicStats(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeMenloVnicStats")

	@staticmethod
	def ClassId():
		return "apeMenloVnicStats"

	BYTES_EG = "Bytes_eg"
	BYTES_IN = "Bytes_in"
	DN = "Dn"
	DROPPED_PKTS_EG = "Dropped_pkts_eg"
	DROPPED_PKTS_IN = "Dropped_pkts_in"
	ERRORS_EG = "Errors_eg"
	ERRORS_IN = "Errors_in"
	PKTS_EG = "Pkts_eg"
	PKTS_IN = "Pkts_in"
	RN = "Rn"
	STATUS = "Status"

