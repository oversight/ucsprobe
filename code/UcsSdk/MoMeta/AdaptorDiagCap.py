import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AdaptorDiagCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"AdaptorDiagCap")

	@staticmethod
	def ClassId():
		return "adaptorDiagCap"

	DN = "Dn"
	ENABLE_LLDP_TRANSMIT = "EnableLldpTransmit"
	RN = "Rn"
	STATUS = "Status"

	CONST_ENABLE_LLDP_TRANSMIT_FALSE = "false"
	CONST_ENABLE_LLDP_TRANSMIT_NO = "no"
	CONST_ENABLE_LLDP_TRANSMIT_TRUE = "true"
	CONST_ENABLE_LLDP_TRANSMIT_YES = "yes"
