import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentDiscoveryCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentDiscoveryCap")

	@staticmethod
	def ClassId():
		return "equipmentDiscoveryCap"

	DN = "Dn"
	OPER_POWER_REQUIREMENT = "OperPowerRequirement"
	RN = "Rn"
	STATUS = "Status"

	CONST_OPER_POWER_REQUIREMENT_FULL = "full"
	CONST_OPER_POWER_REQUIREMENT_NONE = "none"
	CONST_OPER_POWER_REQUIREMENT_STANDBY = "standby"
