import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentGemPortCap(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentGemPortCap")

	@staticmethod
	def ClassId():
		return "equipmentGemPortCap"

	DESCR = "Descr"
	DN = "Dn"
	MAX_FC_SPEED = "MaxFcSpeed"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	PORT_NUMBER = "PortNumber"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_MAX_FC_SPEED_1GBPS = "1gbps"
	CONST_MAX_FC_SPEED_2GBPS = "2gbps"
	CONST_MAX_FC_SPEED_4GBPS = "4gbps"
	CONST_MAX_FC_SPEED_8GBPS = "8gbps"
	CONST_MAX_FC_SPEED_AUTO = "auto"
	CONST_MAX_FC_SPEED_INDETERMINATE = "indeterminate"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
