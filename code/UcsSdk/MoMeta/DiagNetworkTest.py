import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DiagNetworkTest(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"DiagNetworkTest")

	@staticmethod
	def ClassId():
		return "diagNetworkTest"

	DN = "Dn"
	LENGTH = "Length"
	ORDER = "Order"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TYPE = "Type"

	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_TYPE_ETH = "eth"
	CONST_TYPE_FC = "fc"
