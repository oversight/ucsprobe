import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorFcPortPLogiProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorFcPortPLogiProfile")

	@staticmethod
	def ClassId():
		return "adaptorFcPortPLogiProfile"

	DN = "Dn"
	RETRIES = "Retries"
	RN = "Rn"
	STATUS = "Status"
	TIMEOUT = "Timeout"

