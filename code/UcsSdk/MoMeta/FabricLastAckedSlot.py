import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FabricLastAckedSlot(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"FabricLastAckedSlot")

	@staticmethod
	def ClassId():
		return "fabricLastAckedSlot"

	BOARD_AGGREGATION_ROLE = "BoardAggregationRole"
	CHASSIS_ID = "ChassisId"
	DN = "Dn"
	RN = "Rn"
	SLOT_ID = "SlotId"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"

	CONST_BOARD_AGGREGATION_ROLE_MULTI_MASTER = "multi-master"
	CONST_BOARD_AGGREGATION_ROLE_MULTI_SLAVE = "multi-slave"
	CONST_BOARD_AGGREGATION_ROLE_NONE = "none"
	CONST_BOARD_AGGREGATION_ROLE_SINGLE = "single"
	CONST_CHASSIS_ID_N_A = "N/A"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
