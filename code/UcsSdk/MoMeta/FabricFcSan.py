import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricFcSan(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricFcSan")

	@staticmethod
	def ClassId():
		return "fabricFcSan"

	DN = "Dn"
	ID = "Id"
	LOCALE = "Locale"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"
	TRANSPORT = "Transport"
	TYPE = "Type"
	UPLINK_TRUNKING = "UplinkTrunking"

	CONST_ID_A = "A"
	CONST_ID_B = "B"
	CONST_ID_NONE = "NONE"
	CONST_UPLINK_TRUNKING_DISABLED = "disabled"
	CONST_UPLINK_TRUNKING_ENABLED = "enabled"
