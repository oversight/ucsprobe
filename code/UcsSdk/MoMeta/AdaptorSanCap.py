import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorSanCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorSanCap")

	@staticmethod
	def ClassId():
		return "adaptorSanCap"

	DN = "Dn"
	HOST_NVRAM = "HostNvram"
	RN = "Rn"
	STATUS = "Status"

	CONST_HOST_NVRAM_FULL = "full"
	CONST_HOST_NVRAM_NONE = "none"
