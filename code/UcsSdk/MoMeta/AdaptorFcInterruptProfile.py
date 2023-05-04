import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorFcInterruptProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorFcInterruptProfile")

	@staticmethod
	def ClassId():
		return "adaptorFcInterruptProfile"

	DN = "Dn"
	MODE = "Mode"
	RN = "Rn"
	STATUS = "Status"

	CONST_MODE_INTX = "intx"
	CONST_MODE_MSI = "msi"
	CONST_MODE_MSI_X = "msi-x"
