import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEthCompQueueProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEthCompQueueProfile")

	@staticmethod
	def ClassId():
		return "adaptorEthCompQueueProfile"

	COUNT = "Count"
	DN = "Dn"
	RING_SIZE = "RingSize"
	RN = "Rn"
	STATUS = "Status"

