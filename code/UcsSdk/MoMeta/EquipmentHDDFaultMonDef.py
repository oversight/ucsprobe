import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EquipmentHDDFaultMonDef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"EquipmentHDDFaultMonDef")

	@staticmethod
	def ClassId():
		return "equipmentHDDFaultMonDef"

	_CONTROLLER_FW_VERSION = "ControllerFwVersion"
	_CONTROLLER_MODEL = "ControllerModel"
	_HDDMON_SUPPORT = "HDDMonSupport"
	DESCR = "Descr"
	DN = "Dn"
	NAME = "Name"
	POLICY_LEVEL = "PolicyLevel"
	POLICY_OWNER = "PolicyOwner"
	RN = "Rn"
	STATUS = "Status"

	CONST_INT_ID_NONE = "none"
	CONST_POLICY_OWNER_LOCAL = "local"
	CONST_POLICY_OWNER_PENDING_POLICY = "pending-policy"
	CONST_POLICY_OWNER_POLICY = "policy"
