import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentIndicatorLed(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentIndicatorLed")

	@staticmethod
	def ClassId():
		return "equipmentIndicatorLed"

	COLOR = "Color"
	DN = "Dn"
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
	CONST_OPER_STATE_BLINKING = "blinking"
	CONST_OPER_STATE_ETH = "eth"
	CONST_OPER_STATE_FC = "fc"
	CONST_OPER_STATE_OFF = "off"
	CONST_OPER_STATE_ON = "on"
	CONST_OPER_STATE_UNKNOWN = "unknown"
