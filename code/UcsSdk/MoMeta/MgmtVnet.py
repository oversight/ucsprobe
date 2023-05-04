import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UcsBase import ManagedObject
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MgmtVnet(ManagedObject):
	def __init__(self):
		ManagedObject.__init__(self,"MgmtVnet")

	@staticmethod
	def ClassId():
		return "mgmtVnet"

	CONFIG_STATE = "ConfigState"
	DN = "Dn"
	ID = "Id"
	NAME = "Name"
	RN = "Rn"
	STATUS = "Status"

	CONST_CONFIG_STATE_INCOMPLETE = "incomplete"
	CONST_CONFIG_STATE_UNRESOLVED_VLAN = "unresolvedVlan"
	CONST_CONFIG_STATE_UNSUPPORTED_FIRMWARE = "unsupportedFirmware"
	CONST_CONFIG_STATE_UNSUPPORTED_SERVER = "unsupportedServer"
	CONST_CONFIG_STATE_UNSUPPORTED_VLAN = "unsupportedVlan"
	CONST_CONFIG_STATE_VALID = "valid"
