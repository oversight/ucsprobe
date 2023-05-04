import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class SwVlanPortNs(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"SwVlanPortNs")

	@staticmethod
	def ClassId():
		return "swVlanPortNs"

	ACCESS_VLAN_PORT_COUNT = "AccessVlanPortCount"
	ALLOC_STATUS = "AllocStatus"
	BORDER_VLAN_PORT_COUNT = "BorderVlanPortCount"
	CONFIG_STATUS = "ConfigStatus"
	DN = "Dn"
	LIMIT = "Limit"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	VLAN_COMP_OFF_LIMIT = "VlanCompOffLimit"
	VLAN_COMP_ON_LIMIT = "VlanCompOnLimit"

	CONST_ALLOC_STATUS_AVAILABLE = "available"
	CONST_ALLOC_STATUS_EXCEEDED = "exceeded"
	CONST_CONFIG_STATUS_NO_VLAN_COMP = "no-vlan-comp"
	CONST_CONFIG_STATUS_NONE = "none"
	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
