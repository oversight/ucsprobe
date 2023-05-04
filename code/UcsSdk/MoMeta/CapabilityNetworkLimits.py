import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CapabilityNetworkLimits(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"CapabilityNetworkLimits")

	@staticmethod
	def ClassId():
		return "capabilityNetworkLimits"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

