import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class VnicDynamicProviderEp(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"VnicDynamicProviderEp")

	@staticmethod
	def ClassId():
		return "vnicDynamicProviderEp"

	CHASSIS_ID = "ChassisId"
	DN = "Dn"
	PORT_ID = "PortId"
	RN = "Rn"
	SLOT_ID = "SlotId"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"

	CONST_CHASSIS_ID_N_A = "N/A"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
