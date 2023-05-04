import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorFcPortFLogiProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorFcPortFLogiProfile")

	@staticmethod
	def ClassId():
		return "adaptorFcPortFLogiProfile"

	DN = "Dn"
	RETRIES = "Retries"
	RN = "Rn"
	STATUS = "Status"
	TIMEOUT = "Timeout"

	CONST_RETRIES_INFINITE = "infinite"
