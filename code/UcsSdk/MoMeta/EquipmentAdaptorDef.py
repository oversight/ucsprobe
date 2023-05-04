import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentAdaptorDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentAdaptorDef")

	@staticmethod
	def ClassId():
		return "equipmentAdaptorDef"

	DESCR = "Descr"
	DN = "Dn"
	ETHERNET_PORT_SPEED = "EthernetPortSpeed"
	FIBRE_CHANNEL_PORT_SPEED = "FibreChannelPortSpeed"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
