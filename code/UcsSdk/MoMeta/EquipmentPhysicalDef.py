import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentPhysicalDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentPhysicalDef")

	@staticmethod
	def ClassId():
		return "equipmentPhysicalDef"

	DEPTH = "Depth"
	DESCR = "Descr"
	DN = "Dn"
	HEIGHT = "Height"
	MAXIMUM_POWER = "MaximumPower"
	MAXIMUM_TEMPERATURE = "MaximumTemperature"
	MINIMUM_POWER = "MinimumPower"
	MINIMUM_TEMPERATURE = "MinimumTemperature"
	NAME = "Name"
	NOMINAL_POWER = "NominalPower"
	NOMINAL_TEMPERATURE = "NominalTemperature"
	OPERATING_VOLTAGES = "OperatingVoltages"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"
	WEIGHT = "Weight"
	WIDTH = "Width"

	CONST_DEPTH_NOT_APPLICABLE = "not-applicable"
	CONST_HEIGHT_NOT_APPLICABLE = "not-applicable"
	CONST_INT_ID_NONE = "none"
	CONST_MAXIMUM_POWER_NOT_APPLICABLE = "not-applicable"
	CONST_MAXIMUM_TEMPERATURE_NOT_APPLICABLE = "not-applicable"
	CONST_MINIMUM_POWER_NOT_APPLICABLE = "not-applicable"
	CONST_MINIMUM_TEMPERATURE_NOT_APPLICABLE = "not-applicable"
	CONST_NOMINAL_POWER_NOT_APPLICABLE = "not-applicable"
	CONST_NOMINAL_TEMPERATURE_NOT_APPLICABLE = "not-applicable"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
	CONST_WEIGHT_NOT_APPLICABLE = "not-applicable"
	CONST_WIDTH_NOT_APPLICABLE = "not-applicable"
