import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StorageVsanRef(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"StorageVsanRef")

	@staticmethod
	def ClassId():
		return "storageVsanRef"

	CONFIG_QUALIFIER = "ConfigQualifier"
	DN = "Dn"
	NAME = "Name"
	OPER_VNET_DN = "OperVnetDn"
	OPER_VNET_NAME = "OperVnetName"
	RN = "Rn"
	STATUS = "Status"
	SWITCH_ID = "SwitchId"
	VNET = "Vnet"
	ZONING_STATE = "ZoningState"

	CONST_SWITCH_ID_A = "A"
	CONST_SWITCH_ID_B = "B"
	CONST_SWITCH_ID_NONE = "NONE"
	CONST_SWITCH_ID_DUAL = "dual"
	CONST_ZONING_STATE_DISABLED = "disabled"
	CONST_ZONING_STATE_ENABLED = "enabled"
