import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentHealthLed(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentHealthLed")

	@staticmethod
	def ClassId():
		return "equipmentHealthLed"

	COLOR = "Color"
	DN = "Dn"
	HEALTH_LED_STATE = "HealthLedState"
	HEALTH_LED_STATE_QUALIFIER = "HealthLedStateQualifier"
	ID = "Id"
	NAME = "Name"
	OPER_STATE = "OperState"
	RN = "Rn"
	STATUS = "Status"

	CONST_COLOR_AMBER = "amber"
	CONST_COLOR_BLUE = "blue"
	CONST_COLOR_GREEN = "green"
	CONST_COLOR_RED = "red"
	CONST_COLOR_UNKNOWN = "unknown"
	CONST_HEALTH_LED_STATE_CRITICAL = "critical"
	CONST_HEALTH_LED_STATE_MINOR = "minor"
	CONST_HEALTH_LED_STATE_NORMAL = "normal"
	CONST_OPER_STATE_BLINKING = "blinking"
	CONST_OPER_STATE_ETH = "eth"
	CONST_OPER_STATE_FC = "fc"
	CONST_OPER_STATE_OFF = "off"
	CONST_OPER_STATE_ON = "on"
	CONST_OPER_STATE_UNKNOWN = "unknown"
