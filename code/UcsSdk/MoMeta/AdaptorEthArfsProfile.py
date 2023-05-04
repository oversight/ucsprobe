import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorEthArfsProfile(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorEthArfsProfile")

	@staticmethod
	def ClassId():
		return "adaptorEthArfsProfile"

	ACCELARATED_RFS = "AccelaratedRFS"
	DN = "Dn"
	RN = "Rn"
	STATUS = "Status"

	CONST_ACCELARATED_RFS_DISABLED = "disabled"
	CONST_ACCELARATED_RFS_ENABLED = "enabled"
