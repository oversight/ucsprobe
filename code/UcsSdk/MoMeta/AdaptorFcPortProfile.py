import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorFcPortProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorFcPortProfile")

	@staticmethod
	def ClassId():
		return "adaptorFcPortProfile"

	DN = "Dn"
	IO_THROTTLE_COUNT = "IoThrottleCount"
	LUNS_PER_TARGET = "LunsPerTarget"
	RN = "Rn"
	STATUS = "Status"

