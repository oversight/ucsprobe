import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PortTrustMode(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"PortTrustMode")

	@staticmethod
	def ClassId():
		return "portTrustMode"

	DN = "Dn"
	RN = "Rn"
	STATE = "State"
	STATUS = "Status"

	CONST_STATE_TRUSTED = "trusted"
	CONST_STATE_UNTRUSTED = "untrusted"
