import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AaaDomain(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AaaDomain")

	@staticmethod
	def ClassId():
		return "aaaDomain"

	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	REFRESH_PERIOD = "RefreshPeriod"
	RN = "Rn"
	SESSION_TIMEOUT = "SessionTimeout"
	STATUS = "Status"

