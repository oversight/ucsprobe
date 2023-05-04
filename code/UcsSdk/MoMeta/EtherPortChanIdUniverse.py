import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EtherPortChanIdUniverse(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EtherPortChanIdUniverse")

	@staticmethod
	def ClassId():
		return "etherPortChanIdUniverse"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

