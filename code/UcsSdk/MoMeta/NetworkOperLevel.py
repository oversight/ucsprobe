import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class NetworkOperLevel(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"NetworkOperLevel")

	@staticmethod
	def ClassId():
		return "networkOperLevel"

	DN = "Dn"
	ID = "Id"
	MAX_PRIMARY_VLAN_COUNT = "MaxPrimaryVlanCount"
	MAX_SEC_VLAN_PER_PRIMARY_VLAN_COUNT = "MaxSecVlanPerPrimaryVlanCount"
	MAX_SECONDARY_VLAN_COUNT = "MaxSecondaryVlanCount"
	PRIMARY_VLAN_COUNT = "PrimaryVlanCount"
	PRIMARY_VLAN_COUNT_STATUS = "PrimaryVlanCountStatus"
	RN = "Rn"
	SECONDARY_VLAN_COUNT = "SecondaryVlanCount"
	SECONDARY_VLAN_COUNT_STATUS = "SecondaryVlanCountStatus"
	STATUS = "Status"

	CONST_ID_A = "A"
	CONST_ID_B = "B"
	CONST_ID_NONE = "NONE"
	CONST_PRIMARY_VLAN_COUNT_STATUS_ABOVE_LIMIT = "above-limit"
	CONST_PRIMARY_VLAN_COUNT_STATUS_WITHIN_LIMIT = "within-limit"
	CONST_SECONDARY_VLAN_COUNT_STATUS_ABOVE_LIMIT = "above-limit"
	CONST_SECONDARY_VLAN_COUNT_STATUS_WITHIN_LIMIT = "within-limit"
