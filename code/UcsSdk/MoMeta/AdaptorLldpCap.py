import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorLldpCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorLldpCap")

	@staticmethod
	def ClassId():
		return "adaptorLldpCap"

	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"
	SUPPORT = "Support"

	CONST_SUPPORT_FULL = "full"
	CONST_SUPPORT_NONE = "none"
