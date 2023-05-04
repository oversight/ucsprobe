import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ApeHostAgent(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"ApeHostAgent")

	@staticmethod
	def ClassId():
		return "apeHostAgent"

	CHASSIS_ID = "ChassisId"
	DN = "Dn"
	RN = "Rn"
	SERVER_ID = "ServerId"
	SLOT_ID = "SlotId"
	STATE = "State"
	STATUS = "Status"

	CONST_CHASSIS_ID_N_A = "N/A"
	CONST_STATE_HALTING_HOSTOS = "HALTING_HOSTOS"
	CONST_STATE_HALTING_PNUOS = "HALTING_PNUOS"
	CONST_STATE_HOSTOS = "HOSTOS"
	CONST_STATE_PNUOS = "PNUOS"
	CONST_STATE_STARTING_HOSTOS = "STARTING_HOSTOS"
	CONST_STATE_STARTING_PNUOS = "STARTING_PNUOS"
	CONST_STATE_UNKNOWN = "UNKNOWN"
