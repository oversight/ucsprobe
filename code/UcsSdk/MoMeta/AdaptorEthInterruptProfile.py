import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEthInterruptProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEthInterruptProfile")

	@staticmethod
	def ClassId():
		return "adaptorEthInterruptProfile"

	COALESCING_TIME = "CoalescingTime"
	COALESCING_TYPE = "CoalescingType"
	COUNT = "Count"
	DN = "Dn"
	MODE = "Mode"
	RN = "Rn"
	STATUS = "Status"

	CONST_COALESCING_TYPE_IDLE = "idle"
	CONST_COALESCING_TYPE_MIN = "min"
	CONST_MODE_INTX = "intx"
	CONST_MODE_MSI = "msi"
	CONST_MODE_MSI_X = "msi-x"
