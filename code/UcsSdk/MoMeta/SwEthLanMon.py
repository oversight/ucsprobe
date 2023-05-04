import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwEthLanMon(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwEthLanMon")

	@staticmethod
	def ClassId():
		return "swEthLanMon"

	DN = "Dn"
	LOCALE = "Locale"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	TRANSPORT = "Transport"
	TYPE = "Type"

	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
