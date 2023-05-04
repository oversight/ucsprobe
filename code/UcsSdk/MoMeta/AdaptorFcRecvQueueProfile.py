import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorFcRecvQueueProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorFcRecvQueueProfile")

	@staticmethod
	def ClassId():
		return "adaptorFcRecvQueueProfile"

	COUNT = "Count"
	DN = "Dn"
	RING_SIZE = "RingSize"
	RN = "Rn"
	STATUS = "Status"

